# This module contains user level functions related to the stacking of the
# input dataset

import sys
import math
import numpy as np
from astrodata import Errors
from astrodata import Lookups
from astrodata.adutils import gemLog
from astrodata.adutils.gemutil import pyrafLoader
from gempy import geminiTools as gt
from gempy import managers as mgr
from gempy.geminiCLParDicts import CLDefaultParamsDict

# Load the timestamp keyword dictionary that will be used to define the keyword
# to be used for the time stamp for the user level function
timestamp_keys = Lookups.get_lookup_table("Gemini/timestamp_keywords",
                                          "timestamp_keys")

def stack_frames(adinput=None, suffix=None, operation="average", 
                 reject_method="avsigclip", mask_type="goodvalue",
                 nlow=1, nhigh=1, grow=0.0):
    """
    This user level function will stack the input AstroData objects. New
    variance extensions are created from the stacked science extensions and the
    data quality extensions are propagated to the output AstroData object.
    
    NOTE: The inputs to this function MUST be prepared.
    
    :param adinput: Astrodata inputs to be combined
    :type adinput: Astrodata objects, either a single or a list of objects
    
    :param operation: type of combining operation to use.
    :type operation: string, options: 'average', 'median'.
    """
    
    # Instantiate the log. This needs to be done outside of the try block,
    # since the log object is used in the except block 
    log = gemLog.getGeminiLog()
    
    # The validate_input function ensures that the input is not None and
    # returns a list containing one or more AstroData objects
    adinput = gt.validate_input(adinput=adinput)
    
    # Check whether two or more input AstroData objects were provided
    if len(adinput) == 1:
        msg = "No stacking will be performed, since at least two input " \
              "AstroData objects are required for stack_frames"
        raise Errors.InputError(msg)
    
    # Define the keyword to be used for the time stamp for this user level
    # function
    timestamp_key = timestamp_keys["stack_frames"]
    
    # Initialize the list of output AstroData objects
    adoutput_list = []
    
    try:

        # Get average of current GAIN parameters from input files
        # and add in quadrature the read-out noise
        gain = adinput[0].gain().as_dict()
        ron = adinput[0].read_noise().as_dict()
        for ad in adinput[1:]:
            for ext in ad["SCI"]:
                gain[("SCI",ext.extver())] += ext.gain()
                ron[("SCI",ext.extver())] += ext.read_noise()**2
        for key in gain.keys():
            gain[key] /= len(adinput)
            ron[key] = math.sqrt(ron[key])

        # Load PyRAF
        pyraf, gemini, yes, no = pyrafLoader()
        # Use the CL manager to get the input parameters
        clm = mgr.CLManager(imageIns=adinput, funcName="combine",
                            suffix=suffix, combinedImages=True, log=log)
        if not clm.status:
            raise Errors.InputError("Please provide prepared inputs")
        
        # Get the input parameters for IRAF as specified by the stackFrames
        # primitive 
        clPrimParams = {
            # Retrieving the inputs as a list from the CLManager
            "input"   : clm.imageInsFiles(type="listFile"),
            # Maybe allow the user to override this in the future
            "output"  : clm.imageOutsFiles(type="string"),
            # This returns a unique/temp log file for IRAF
            "logfile" : clm.templog.name,
            }
        
        # Get the input parameters for IRAF as specified by the user
        fl_vardq = no
        fl_dqprop = no
        for ad in adinput:
            if ad["DQ"]:
                fl_dqprop = yes
                if ad["VAR"]:
                    fl_vardq = yes
        clSoftcodedParams = {
            "fl_vardq"  : fl_vardq,
            "fl_dqprop" : fl_dqprop,
            "combine"   : operation,
            "reject"    : reject_method,
            "nlow"      : nlow,
            "nhigh"     : nhigh,
            "grow"      : grow,
            "masktype"  : mask_type,
            }
        
        # Get the default parameters for IRAF and update them using the above
        # dictionaries
        clParamsDict = CLDefaultParamsDict("gemcombine")
        clParamsDict.update(clPrimParams)
        clParamsDict.update(clSoftcodedParams)
        # Log the parameters
        mgr.logDictParams(clParamsDict)
        # Call gemcombine
        gemini.gemcombine(**clParamsDict)
        if gemini.gemcombine.status:
            raise Errors.OutputError("The IRAF task gemcombine failed")
        else:
            log.fullinfo("The IRAF task gemcombine completed sucessfully")
        
        # Create the output AstroData object by loading the output file from
        # gemcombine into AstroData, remove intermediate temporary files from
        # disk 
        adstack, junk, junk = clm.finishCL()
        
        # Change type of DQ plane back to int16 (gemcombine sets it to int32)
        if adstack[0]["DQ"] is not None:
            for dqext in adstack[0]["DQ"]:
                dqext.data = dqext.data.astype(np.int16)

                # Also delete the BUNIT keyword (gemcombine
                # sets it to same value as SCI)
                if dqext.get_key_value("BUNIT") is not None:
                    del dqext.header['BUNIT']

        # Fix BUNIT in VAR plane as well
        # (gemcombine sets it to same value as SCI)
        bunit = adstack[0]["SCI",1].get_key_value("BUNIT")
        if adstack[0]["VAR"] is not None:
            gt.update_key_value(adinput=adstack[0], function="bunit",
                                value="%s*%s" % (bunit,bunit),
                                extname="VAR")

        # Gemcombine sets the GAIN keyword to the sum of the gains; reset
        # it to the average instead.  Set the RDNOISE to the sum in 
        # quadrature of the input read noise. Set VAR/DQ keywords to 
        # the same as the science.
        for ext in adstack[0]:
            ext.set_key_value("GAIN", gain[("SCI",ext.extver())])
            ext.set_key_value("RDNOISE", ron[("SCI",ext.extver())])
            
        if adstack[0].phu_get_key_value("GAIN") is not None:
            adstack[0].phu_set_key_value("GAIN",gain[("SCI",1)])
        if adstack[0].phu_get_key_value("RDNOISE") is not None:
            adstack[0].phu_set_key_value("RDNOISE",ron[("SCI",1)])

        # Add suffix to the ORIGNAME header so future filenames
        # can't strip it out
        adstack[0].phu_set_key_value("ORIGNAME",
                                     gt.fileNameUpdater(ad,suffix=suffix,
                                                        strip=True),
                                     comment="Original filename")

        # Add the appropriate time stamps to the PHU
        gt.mark_history(adinput=adstack, keyword=timestamp_key)
        
        # Return the output AstroData object
        return adstack
    
    except:
        # Log the message from the exception
        log.critical(repr(sys.exc_info()[1]))
        raise
