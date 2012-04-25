import sys
from astrodata import Descriptors
from astrodata.Descriptors import DescriptorValue
from astrodata import Errors

class CalculatorInterface:

    descriptor_calculator = None

    def airmass(self, format=None, **args):
        """
        Return the airmass value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
        :type format: string
        :rtype: float as default (i.e., format=None)
        :return: the mean airmass of the observation
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"airmass"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "airmass")
            if not hasattr(self.descriptor_calculator, "airmass"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for airmass"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.airmass(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "airmass",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = float )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def amp_read_area(self, format=None, **args):
        """
        Return the amp_read_area value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
                       set to as_dict to return a dictionary, where the number 
                       of dictionary elements equals the number of pixel data 
                       extensions in the image. The key of the dictionary is 
                       an (EXTNAME, EXTVER) tuple, if available. Otherwise, 
                       the key is the integer index of the extension.
        :type format: string
        :rtype: string as default (i.e., format=None)
        :rtype: dictionary containing one or more string(s) (format=as_dict)
        :return: the composite string containing the name of the detector
                 amplifier (ampname) and the readout area of the CCD (detsec) 
                 used for the observation
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"amp_read_area"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "amp_read_area")
            if not hasattr(self.descriptor_calculator, "amp_read_area"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for amp_read_area"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.amp_read_area(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "amp_read_area",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = str )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def array_section(self, format=None, **args):
        """
        Return the array_section value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
        :type format: string
        :rtype: list as default (i.e., format=None)
        :return: the array_section
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"array_section"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "array_section")
            if not hasattr(self.descriptor_calculator, "array_section"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for array_section"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.array_section(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "array_section",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = list )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def azimuth(self, format=None, **args):
        """
        Return the azimuth value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
        :type format: string
        :rtype: float as default (i.e., format=None)
        :return: the azimuth (in degrees between 0 and 360) of the observation
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"azimuth"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "azimuth")
            if not hasattr(self.descriptor_calculator, "azimuth"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for azimuth"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.azimuth(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "azimuth",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = float )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def bias_level(self, format=None, **args):
        """
        Return the bias_level value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
        :type format: string
        :rtype: float as default (i.e., format=None)
        :return: the bias_level
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"bias_level"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "bias_level")
            if not hasattr(self.descriptor_calculator, "bias_level"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for bias_level"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.bias_level(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "bias_level",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = float )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def camera(self, format=None, **args):
        """
        Return the camera value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
        :type format: string
        :rtype: string as default (i.e., format=None)
        :return: the camera used for the observation
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"camera"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "camera")
            if not hasattr(self.descriptor_calculator, "camera"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for camera"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.camera(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "camera",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = str )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def cass_rotator_pa(self, format=None, **args):
        """
        Return the cass_rotator_pa value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
        :type format: string
        :rtype: float as default (i.e., format=None)
        :return: the cassegrain rotator position angle (in degrees between -360
                 and 360) of the observation
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"cass_rotator_pa"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "cass_rotator_pa")
            if not hasattr(self.descriptor_calculator, "cass_rotator_pa"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for cass_rotator_pa"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.cass_rotator_pa(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "cass_rotator_pa",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = float )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def central_wavelength(self, format=None, **args):
        """
        Return the central_wavelength value
        :param dataset: the data set
        :type dataset: AstroData
        :param asMicrometers: set to True to return the central_wavelength 
                              value in units of Micrometers
        :type asMicrometers: Python boolean
        :param asNanometers: set to True to return the central_wavelength 
                             value in units of Nanometers
        :type asNanometers: Python boolean
        :param asAngstroms: set to True to return the central_wavelength 
                            value in units of Angstroms
        :type asAngstroms: Python boolean
        :param format: set to as_dict to return a dictionary, where the number 
                       of dictionary elements equals the number of pixel data 
                       extensions in the image. The key of the dictionary is 
                       an (EXTNAME, EXTVER) tuple, if available. Otherwise, 
                       the key is the integer index of the extension.
        :type format: string
        :rtype: float as default (i.e., format=None)
        :rtype: dictionary containing one or more float(s)
        :return: the central wavelength (in meters as default) of the 
                 observation
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"central_wavelength"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "central_wavelength")
            if not hasattr(self.descriptor_calculator, "central_wavelength"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for central_wavelength"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.central_wavelength(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "central_wavelength",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = float )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def coadds(self, format=None, **args):
        """
        Return the coadds value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
        :type format: string
        :rtype: integer as default (i.e., format=None)
        :return: the number of coadds used for the observation
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"coadds"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "coadds")
            if not hasattr(self.descriptor_calculator, "coadds"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for coadds"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.coadds(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "coadds",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = int )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def data_label(self, format=None, **args):
        """
        Return the data_label value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
        :type format: string
        :rtype: string as default (i.e., format=None)
        :return: the data label of the observation
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"data_label"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "data_label")
            if not hasattr(self.descriptor_calculator, "data_label"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for data_label"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.data_label(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "data_label",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = str )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def data_section(self, format=None, **args):
        """
        Return the data_section value
        :param dataset: the data set
        :type dataset: AstroData
        :param pretty: set to True to return a human meaningful data_section 
                       value in the form [x1:x2,y1:y2] that uses 1-based 
                       indexing
        :type pretty: Python boolean
        :param format: set to as_dict to return a dictionary, where the number 
                       of dictionary elements equals the number of pixel data 
                       extensions in the image. The key of the dictionary is 
                       an (EXTNAME, EXTVER) tuple, if available. Otherwise, 
                       the key is the integer index of the extension.
        :type format: string
        :rtype: tuple of integers that use 0-based indexing in the form 
                (x1 - 1, x2 - 1, y1 - 1, y2 - 1) as default 
                (i.e., format=None, pretty=False)
        :rtype: string that uses 1-based indexing in the form [x1:x2,y1:y2] 
                (pretty=True)
        :rtype: dictionary containing one or more of the above return types 
                (format=as_dict)
        :return: the section of the data of the observation
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"data_section"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "data_section")
            if not hasattr(self.descriptor_calculator, "data_section"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for data_section"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.data_section(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "data_section",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = list )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def dec(self, format=None, **args):
        """
        Return the dec value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
        :type format: string
        :rtype: float as default (i.e., format=None)
        :return: the declination (in decimal degrees) of the observation
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"dec"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "dec")
            if not hasattr(self.descriptor_calculator, "dec"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for dec"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.dec(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "dec",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = float )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def decker(self, format=None, **args):
        """
        Return the decker value
        :param dataset: the data set
        :type dataset: AstroData
        :param stripID: set to True to remove the component ID from the 
                        returned decker value
        :type stripID: Python boolean
        :param pretty: set to True to return a human meaningful 
                       decker value
        :type pretty: Python boolean
        :rtype: string as default (i.e., format=None)
        :return: the decker position used for the observation
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"decker"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "decker")
            if not hasattr(self.descriptor_calculator, "decker"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for decker"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.decker(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "decker",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = str )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def detector_rois_requested(self, format=None, **args):
        """
        Return the detector_rois_requested value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
        :type format: string
        :rtype: list as default (i.e., format=None)
        :return: the detector_rois_requested
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"detector_rois_requested"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "detector_rois_requested")
            if not hasattr(self.descriptor_calculator, "detector_rois_requested"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for detector_rois_requested"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.detector_rois_requested(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "detector_rois_requested",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = list )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def detector_roi_setting(self, format=None, **args):
        """
        Return the detector_roi_setting value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
        :type format: string
        :rtype: string as default (i.e., format=None)
        :return: the detector_roi_setting
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"detector_roi_setting"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "detector_roi_setting")
            if not hasattr(self.descriptor_calculator, "detector_roi_setting"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for detector_roi_setting"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.detector_roi_setting(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "detector_roi_setting",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = str )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def detector_section(self, format=None, **args):
        """
        Return the detector_section value
        :param dataset: the data set
        :type dataset: AstroData
        :param pretty: set to True to return a human meaningful 
                       detector_section value in the form [x1:x2,y1:y2] that 
                       uses 1-based indexing
        :type pretty: Python boolean
        :param format: set to as_dict to return a dictionary, where the number 
                       of dictionary elements equals the number of pixel data 
                       extensions in the image. The key of the dictionary is 
                       an (EXTNAME, EXTVER) tuple, if available. Otherwise, 
                       the key is the integer index of the extension.
        :type format: string
        :rtype: tuple of integers that use 0-based indexing in the form 
                (x1 - 1, x2 - 1, y1 - 1, y2 - 1) as default 
                (i.e., format=None, pretty=False)
        :rtype: string that uses 1-based indexing in the form [x1:x2,y1:y2] 
                (pretty=True)
        :rtype: dictionary containing one or more of the above return types 
                (format=as_dict)
        :return: the detector section of the observation
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"detector_section"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "detector_section")
            if not hasattr(self.descriptor_calculator, "detector_section"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for detector_section"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.detector_section(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "detector_section",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = list )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def detector_name(self, format=None, **args):
        """
        Return the detector_name value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
        :type format: string
        :rtype: string as default (i.e., format=None)
        :return: the detector_name
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"detector_name"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "detector_name")
            if not hasattr(self.descriptor_calculator, "detector_name"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for detector_name"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.detector_name(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "detector_name",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = str )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def detector_x_bin(self, format=None, **args):
        """
        Return the detector_x_bin value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
                       set to as_dict to return a dictionary, where the number 
                       of dictionary elements equals the number of pixel data 
                       extensions in the image. The key of the dictionary is 
                       an (EXTNAME, EXTVER) tuple, if available. Otherwise, 
                       the key is the integer index of the extension.
        :type format: string
        :rtype: integer as default (i.e., format=None)
        :rtype: dictionary containing one or more integer(s) (format=as_dict)
        :return: the binning of the x-axis of the detector used for the 
                 observation
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"detector_x_bin"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "detector_x_bin")
            if not hasattr(self.descriptor_calculator, "detector_x_bin"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for detector_x_bin"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.detector_x_bin(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "detector_x_bin",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = int )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def detector_y_bin(self, format=None, **args):
        """
        Return the detector_y_bin value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
                       set to as_dict to return a dictionary, where the number 
                       of dictionary elements equals the number of pixel data 
                       extensions in the image. The key of the dictionary is 
                       an (EXTNAME, EXTVER) tuple, if available. Otherwise, 
                       the key is the integer index of the extension.
        :type format: string
        :rtype: integer as default (i.e., format=None)
        :rtype: dictionary containing one or more integer(s) (format=as_dict)
        :return: the binning of the y-axis of the detector used for the 
                 observation
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"detector_y_bin"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "detector_y_bin")
            if not hasattr(self.descriptor_calculator, "detector_y_bin"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for detector_y_bin"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.detector_y_bin(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "detector_y_bin",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = int )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def disperser(self, format=None, **args):
        """
        Return the disperser value
        :param dataset: the data set
        :type dataset: AstroData
        :param stripID: set to True to remove the component ID from the 
                        returned disperser value
        :type stripID: Python boolean
        :param pretty: set to True to return a human meaningful 
                       disperser value
        :type pretty: Python boolean
        :rtype: string as default (i.e., format=None)
        :return: the disperser used for the observation
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"disperser"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "disperser")
            if not hasattr(self.descriptor_calculator, "disperser"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for disperser"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.disperser(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "disperser",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = str )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def dispersion(self, format=None, **args):
        """
        Return the dispersion value
        :param dataset: the data set
        :type dataset: AstroData
        :param asMicrometers: set to True to return the dispersion 
                              value in units of Micrometers
        :type asMicrometers: Python boolean
        :param asNanometers: set to True to return the dispersion 
                             value in units of Nanometers
        :type asNanometers: Python boolean
        :param asAngstroms: set to True to return the dispersion 
                            value in units of Angstroms
        :type asAngstroms: Python boolean
        :param format: set to as_dict to return a dictionary, where the number 
                       of dictionary elements equals the number of pixel data 
                       extensions in the image. The key of the dictionary is 
                       an (EXTNAME, EXTVER) tuple, if available. Otherwise, 
                       the key is the integer index of the extension.
        :type format: string
        :rtype: float as default (i.e., format=None)
        :rtype: dictionary containing one or more float(s) (format=as_dict)
        :return: the dispersion (in meters per pixel as default) of the 
                 observation
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"dispersion"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "dispersion")
            if not hasattr(self.descriptor_calculator, "dispersion"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for dispersion"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.dispersion(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "dispersion",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = float )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def dispersion_axis(self, format=None, **args):
        """
        Return the dispersion_axis value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
        :type format: string
        :rtype: integer as default (i.e., format=None)
        :return: the dispersion axis (x = 1; y = 2; z = 3) of the observation
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"dispersion_axis"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "dispersion_axis")
            if not hasattr(self.descriptor_calculator, "dispersion_axis"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for dispersion_axis"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.dispersion_axis(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "dispersion_axis",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = int )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def elevation(self, format=None, **args):
        """
        Return the elevation value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
        :type format: string
        :rtype: float as default (i.e., format=None)
        :return: the elevation (in degrees) of the observation
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"elevation"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "elevation")
            if not hasattr(self.descriptor_calculator, "elevation"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for elevation"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.elevation(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "elevation",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = float )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def exposure_time(self, format=None, **args):
        """
        Return the exposure_time value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
        :type format: string
        :rtype: float as default (i.e., format=None)
        :return: the total exposure time (in seconds) of the observation
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"exposure_time"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "exposure_time")
            if not hasattr(self.descriptor_calculator, "exposure_time"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for exposure_time"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.exposure_time(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "exposure_time",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = float )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def filter_name(self, format=None, **args):
        """
        Return the filter_name value
        :param dataset: the data set
        :type dataset: AstroData
        :param stripID: set to True to remove the component ID from the 
                        returned filter_name value
        :type stripID: Python boolean
        :param pretty: set to True to return a human meaningful 
                       filter_name value
        :type pretty: Python boolean
        :rtype: string as default (i.e., format=None)
        :return: the unique, sorted filter name idenifier string used for the 
                 observation
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"filter_name"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "filter_name")
            if not hasattr(self.descriptor_calculator, "filter_name"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for filter_name"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.filter_name(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "filter_name",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = str )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def focal_plane_mask(self, format=None, **args):
        """
        Return the focal_plane_mask value
        :param dataset: the data set
        :type dataset: AstroData
        :param stripID: set to True to remove the component ID from the 
                        returned focal_plane_mask value
        :type stripID: Python boolean
        :param pretty: set to True to return a human meaningful 
                       focal_plane_mask value
        :type pretty: Python boolean
        :rtype: string as default (i.e., format=None)
        :return: the focal plane mask used for the observation
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"focal_plane_mask"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "focal_plane_mask")
            if not hasattr(self.descriptor_calculator, "focal_plane_mask"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for focal_plane_mask"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.focal_plane_mask(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "focal_plane_mask",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = str )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def gain(self, format=None, **args):
        """
        Return the gain value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
                       set to as_dict to return a dictionary, where the number 
                       of dictionary elements equals the number of pixel data 
                       extensions in the image. The key of the dictionary is 
                       an (EXTNAME, EXTVER) tuple, if available. Otherwise, 
                       the key is the integer index of the extension.
        :type format: string
        :rtype: float as default (i.e., format=None)
        :rtype: dictionary containing one or more float(s) (format=as_dict)
        :return: the gain (in electrons per ADU) of the observation
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"gain"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "gain")
            if not hasattr(self.descriptor_calculator, "gain"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for gain"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.gain(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "gain",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = float )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def grating(self, format=None, **args):
        """
        Return the grating value
        :param dataset: the data set
        :type dataset: AstroData
        :param stripID: set to True to remove the component ID from the 
                        returned grating value
        :type stripID: Python boolean
        :param pretty: set to True to return a human meaningful 
                       grating value
        :type pretty: Python boolean
        :rtype: string as default (i.e., format=None)
        :return: the grating used for the observation
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"grating"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "grating")
            if not hasattr(self.descriptor_calculator, "grating"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for grating"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.grating(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "grating",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = str )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def group_id(self, format=None, **args):
        """
        Return the group_id value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
        :type format: string
        :rtype: string as default (i.e., format=None)
        :return: the group_id
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"group_id"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "group_id")
            if not hasattr(self.descriptor_calculator, "group_id"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for group_id"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.group_id(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "group_id",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = str )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def gain_setting(self, format=None, **args):
        """
        Return the gain_setting value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
        :type format: string
        :rtype: string as default (i.e., format=None)
        :return: the gain setting of the observation
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"gain_setting"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "gain_setting")
            if not hasattr(self.descriptor_calculator, "gain_setting"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for gain_setting"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.gain_setting(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "gain_setting",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = str )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def instrument(self, format=None, **args):
        """
        Return the instrument value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
        :type format: string
        :rtype: string as default (i.e., format=None)
        :return: the instrument used for the observation
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"instrument"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "instrument")
            if not hasattr(self.descriptor_calculator, "instrument"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for instrument"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.instrument(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "instrument",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = str )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def local_time(self, format=None, **args):
        """
        Return the local_time value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
        :type format: string
        :rtype: string as default (i.e., format=None)
        :return: the local time (in HH:MM:SS.S) at the start of the observation
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"local_time"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "local_time")
            if not hasattr(self.descriptor_calculator, "local_time"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for local_time"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.local_time(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "local_time",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = str )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def mdf_row_id(self, format=None, **args):
        """
        Return the mdf_row_id value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
                       set to as_dict to return a dictionary, where the number 
                       of dictionary elements equals the number of pixel data 
                       extensions in the image. The key of the dictionary is 
                       an (EXTNAME, EXTVER) tuple, if available. Otherwise, 
                       the key is the integer index of the extension.
        :type format: string
        :rtype: integer as default (i.e., format=None)
        :rtype: dictionary containing one or more integer(s) (format=as_dict)
        :return: the corresponding reference row in the MDF
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"mdf_row_id"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "mdf_row_id")
            if not hasattr(self.descriptor_calculator, "mdf_row_id"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for mdf_row_id"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.mdf_row_id(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "mdf_row_id",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = int )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def nod_count(self, format=None, **args):
        """
        Return the nod_count value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
        :type format: string
        :rtype: integer as default (i.e., format=None)
        :return: the number of nod and shuffle cycles in the nod and shuffle 
                 observation
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"nod_count"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "nod_count")
            if not hasattr(self.descriptor_calculator, "nod_count"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for nod_count"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.nod_count(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "nod_count",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = int )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def nod_pixels(self, format=None, **args):
        """
        Return the nod_pixels value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
        :type format: string
        :rtype: integer as default (i.e., format=None)
        :return: the number of pixel rows the charge is shuffled by in the nod 
                 and shuffle observation
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"nod_pixels"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "nod_pixels")
            if not hasattr(self.descriptor_calculator, "nod_pixels"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for nod_pixels"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.nod_pixels(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "nod_pixels",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = int )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def nominal_atmospheric_extinction(self, format=None, **args):
        """
        Return the nominal_atmospheric_extinction value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
        :type format: string
        :rtype: float as default (i.e., format=None)
        :return: the nominal_atmospheric_extinction
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"nominal_atmospheric_extinction"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "nominal_atmospheric_extinction")
            if not hasattr(self.descriptor_calculator, "nominal_atmospheric_extinction"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for nominal_atmospheric_extinction"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.nominal_atmospheric_extinction(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "nominal_atmospheric_extinction",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = float )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def nominal_photometric_zeropoint(self, format=None, **args):
        """
        Return the nominal_photometric_zeropoint value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
        :type format: string
        :rtype: float as default (i.e., format=None)
        :return: the nominal_photometric_zeropoint
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"nominal_photometric_zeropoint"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "nominal_photometric_zeropoint")
            if not hasattr(self.descriptor_calculator, "nominal_photometric_zeropoint"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for nominal_photometric_zeropoint"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.nominal_photometric_zeropoint(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "nominal_photometric_zeropoint",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = float )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def non_linear_level(self, format=None, **args):
        """
        Return the non_linear_level value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
        :type format: string
        :rtype: integer as default (i.e., format=None)
        :return: the non linear level in the raw images (in ADU) of the 
                 observation
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"non_linear_level"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "non_linear_level")
            if not hasattr(self.descriptor_calculator, "non_linear_level"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for non_linear_level"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.non_linear_level(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "non_linear_level",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = int )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def object(self, format=None, **args):
        """
        Return the object value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
        :type format: string
        :rtype: string as default (i.e., format=None)
        :return: the name of the target object observed
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"object"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "object")
            if not hasattr(self.descriptor_calculator, "object"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for object"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.object(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "object",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = str )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def observation_class(self, format=None, **args):
        """
        Return the observation_class value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
        :type format: string
        :rtype: string as default (i.e., format=None)
        :return: the class (either 'science', 'progCal', 'partnerCal', 'acq', 
                 'acqCal' or 'dayCal') of the observation
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"observation_class"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "observation_class")
            if not hasattr(self.descriptor_calculator, "observation_class"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for observation_class"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.observation_class(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "observation_class",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = str )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def observation_epoch(self, format=None, **args):
        """
        Return the observation_epoch value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
        :type format: string
        :rtype: string as default (i.e., format=None)
        :return: the epoch (in years) at the start of the observation
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"observation_epoch"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "observation_epoch")
            if not hasattr(self.descriptor_calculator, "observation_epoch"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for observation_epoch"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.observation_epoch(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "observation_epoch",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = str )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def observation_id(self, format=None, **args):
        """
        Return the observation_id value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
        :type format: string
        :rtype: string as default (i.e., format=None)
        :return: the ID (e.g., GN-2011A-Q-123-45) of the observation
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"observation_id"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "observation_id")
            if not hasattr(self.descriptor_calculator, "observation_id"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for observation_id"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.observation_id(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "observation_id",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = str )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def observation_type(self, format=None, **args):
        """
        Return the observation_type value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
        :type format: string
        :rtype: string as default (i.e., format=None)
        :return: the type (either 'OBJECT', 'DARK', 'FLAT', 'ARC', 'BIAS' or 
                 'MASK') of the observation
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"observation_type"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "observation_type")
            if not hasattr(self.descriptor_calculator, "observation_type"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for observation_type"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.observation_type(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "observation_type",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = str )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def overscan_section(self, format=None, **args):
        """
        Return the overscan_section value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
        :type format: string
        :rtype: list as default (i.e., format=None)
        :return: the overscan_section
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"overscan_section"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "overscan_section")
            if not hasattr(self.descriptor_calculator, "overscan_section"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for overscan_section"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.overscan_section(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "overscan_section",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = list )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def pixel_scale(self, format=None, **args):
        """
        Return the pixel_scale value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
        :type format: string
        :rtype: float as default (i.e., format=None)
        :return: the pixel scale (in arcsec per pixel) of the observation
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"pixel_scale"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "pixel_scale")
            if not hasattr(self.descriptor_calculator, "pixel_scale"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for pixel_scale"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.pixel_scale(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "pixel_scale",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = float )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def prism(self, format=None, **args):
        """
        Return the prism value
        :param dataset: the data set
        :type dataset: AstroData
        :param stripID: set to True to remove the component ID from the 
                        returned prism value
        :type stripID: Python boolean
        :param pretty: set to True to return a human meaningful 
                       prism value
        :type pretty: Python boolean
        :rtype: string as default (i.e., format=None)
        :return: the prism used for the observation
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"prism"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "prism")
            if not hasattr(self.descriptor_calculator, "prism"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for prism"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.prism(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "prism",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = str )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def program_id(self, format=None, **args):
        """
        Return the program_id value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
        :type format: string
        :rtype: string as default (i.e., format=None)
        :return: the Gemini program ID (e.g., GN-2011A-Q-123) of the 
                 observation
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"program_id"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "program_id")
            if not hasattr(self.descriptor_calculator, "program_id"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for program_id"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.program_id(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "program_id",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = str )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def pupil_mask(self, format=None, **args):
        """
        Return the pupil_mask value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
        :type format: string
        :rtype: string as default (i.e., format=None)
        :return: the pupil mask used for the observation
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"pupil_mask"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "pupil_mask")
            if not hasattr(self.descriptor_calculator, "pupil_mask"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for pupil_mask"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.pupil_mask(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "pupil_mask",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = str )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def qa_state(self, format=None, **args):
        """
        Return the qa_state value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
        :type format: string
        :rtype: string as default (i.e., format=None)
        :return: the quality assessment state (either 'Undefined', 'Pass', 
                 'Usable', 'Fail' or 'CHECK') of the observation
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"qa_state"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "qa_state")
            if not hasattr(self.descriptor_calculator, "qa_state"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for qa_state"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.qa_state(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "qa_state",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = str )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def ra(self, format=None, **args):
        """
        Return the ra value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
        :type format: string
        :rtype: float as default (i.e., format=None)
        :return: the Right Ascension (in decimal degrees) of the observation
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"ra"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "ra")
            if not hasattr(self.descriptor_calculator, "ra"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for ra"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.ra(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "ra",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = float )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def raw_bg(self, format=None, **args):
        """
        Return the raw_bg value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
        :type format: string
        :rtype: string as default (i.e., format=None)
        :return: the raw background (either '20-percentile', '50-percentile', 
                 '80-percentile' or 'Any') of the observation
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"raw_bg"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "raw_bg")
            if not hasattr(self.descriptor_calculator, "raw_bg"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for raw_bg"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.raw_bg(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "raw_bg",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = str )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def raw_cc(self, format=None, **args):
        """
        Return the raw_cc value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
        :type format: string
        :rtype: string as default (i.e., format=None)
        :return: the raw cloud cover (either '50-percentile', '70-percentile', 
                 '80-percentile', '90-percentile' or 'Any') of the observation
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"raw_cc"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "raw_cc")
            if not hasattr(self.descriptor_calculator, "raw_cc"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for raw_cc"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.raw_cc(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "raw_cc",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = str )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def raw_iq(self, format=None, **args):
        """
        Return the raw_iq value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
        :type format: string
        :rtype: string as default (i.e., format=None)
        :return: the raw image quality (either '20-percentile', 
                 '70-percentile', '85-percentile' or 'Any') of the observation
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"raw_iq"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "raw_iq")
            if not hasattr(self.descriptor_calculator, "raw_iq"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for raw_iq"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.raw_iq(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "raw_iq",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = str )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def raw_wv(self, format=None, **args):
        """
        Return the raw_wv value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
        :type format: string
        :rtype: string as default (i.e., format=None)
        :return: the raw water vapour (either '20-percentile', 
                 '50-percentile', '80-percentile' or 'Any') of the observation
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"raw_wv"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "raw_wv")
            if not hasattr(self.descriptor_calculator, "raw_wv"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for raw_wv"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.raw_wv(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "raw_wv",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = str )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def read_mode(self, format=None, **args):
        """
        Return the read_mode value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
        :type format: string
        :rtype: string as default (i.e., format=None)
        :return: the read mode (either 'Very Faint Object(s)', 
                 'Faint Object(s)', 'Medium Object', 'Bright Object(s)', 
                 'Very Bright Object(s)', 'Low Background', 
                 'Medium Background', 'High Background' or 'Invalid') of the 
                 observation
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"read_mode"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "read_mode")
            if not hasattr(self.descriptor_calculator, "read_mode"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for read_mode"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.read_mode(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "read_mode",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = str )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def read_noise(self, format=None, **args):
        """
        Return the read_noise value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
                       set to as_dict to return a dictionary, where the number 
                       of dictionary elements equals the number of pixel data 
                       extensions in the image. The key of the dictionary is 
                       an (EXTNAME, EXTVER) tuple, if available. Otherwise, 
                       the key is the integer index of the extension.
        :type format: string
        :rtype: float as default (i.e., format=None)
        :rtype: dictionary containing one or more float(s) (format=as_dict)
        :return: the estimated readout noise (in electrons) of the observation
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"read_noise"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "read_noise")
            if not hasattr(self.descriptor_calculator, "read_noise"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for read_noise"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.read_noise(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "read_noise",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = float )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def read_speed_setting(self, format=None, **args):
        """
        Return the read_speed_setting value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
        :type format: string
        :rtype: string as default (i.e., format=None)
        :return: the read speed setting (either 'fast' or 'slow') of the 
                 observation
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"read_speed_setting"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "read_speed_setting")
            if not hasattr(self.descriptor_calculator, "read_speed_setting"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for read_speed_setting"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.read_speed_setting(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "read_speed_setting",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = str )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def requested_iq(self, format=None, **args):
        """
        Return the requested_iq value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
        :type format: string
        :rtype: integer as default (i.e., format=None)
        :return: the requested_iq
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"requested_iq"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "requested_iq")
            if not hasattr(self.descriptor_calculator, "requested_iq"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for requested_iq"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.requested_iq(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "requested_iq",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = int )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def requested_cc(self, format=None, **args):
        """
        Return the requested_cc value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
        :type format: string
        :rtype: integer as default (i.e., format=None)
        :return: the requested_cc
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"requested_cc"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "requested_cc")
            if not hasattr(self.descriptor_calculator, "requested_cc"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for requested_cc"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.requested_cc(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "requested_cc",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = int )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def requested_wv(self, format=None, **args):
        """
        Return the requested_wv value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
        :type format: string
        :rtype: integer as default (i.e., format=None)
        :return: the requested_wv
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"requested_wv"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "requested_wv")
            if not hasattr(self.descriptor_calculator, "requested_wv"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for requested_wv"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.requested_wv(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "requested_wv",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = int )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def requested_bg(self, format=None, **args):
        """
        Return the requested_bg value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
        :type format: string
        :rtype: integer as default (i.e., format=None)
        :return: the requested_bg
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"requested_bg"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "requested_bg")
            if not hasattr(self.descriptor_calculator, "requested_bg"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for requested_bg"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.requested_bg(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "requested_bg",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = int )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def saturation_level(self, format=None, **args):
        """
        Return the saturation_level value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
        :type format: string
        :rtype: integer as default (i.e., format=None)
        :return: the saturation level in the raw images (in ADU) of the 
                 observation
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"saturation_level"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "saturation_level")
            if not hasattr(self.descriptor_calculator, "saturation_level"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for saturation_level"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.saturation_level(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "saturation_level",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = int )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def slit(self, format=None, **args):
        """
        Return the slit value
        :param dataset: the data set
        :type dataset: AstroData
        :param stripID: set to True to remove the component ID from the 
                        returned slit value
        :type stripID: Python boolean
        :param pretty: set to True to return a human meaningful 
                       slit value
        :type pretty: Python boolean
        :rtype: string as default (i.e., format=None)
        :return: the slit used for the observation
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"slit"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "slit")
            if not hasattr(self.descriptor_calculator, "slit"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for slit"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.slit(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "slit",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = str )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def telescope(self, format=None, **args):
        """
        Return the telescope value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
        :type format: string
        :rtype: string as default (i.e., format=None)
        :return: the telescope used for the observation
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"telescope"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "telescope")
            if not hasattr(self.descriptor_calculator, "telescope"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for telescope"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.telescope(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "telescope",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = str )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def ut_date(self, format=None, **args):
        """
        Return the ut_date value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
        :type format: string
        :rtype: datetime as default (i.e., format=None)
        :return: the UT date at the start of the observation
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"ut_date"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "ut_date")
            if not hasattr(self.descriptor_calculator, "ut_date"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for ut_date"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.ut_date(self, **args)
            
            from datetime import datetime
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "ut_date",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = datetime )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def ut_datetime(self, format=None, **args):
        """
        Return the ut_datetime value
        This descriptor attempts to figure out the datetime even when the
        headers are malformed or not present. It tries just about every header
        combination that could allow it to determine an appropriate datetime
        for the file in question. This makes it somewhat specific to Gemini
        data, in that the headers it looks at, and the assumptions it makes in
        trying to parse their values, are those known to occur in Gemini data.
        Note that some of the early gemini data, and that taken from lower
        level engineering interfaces, lack standard headers. Also the format
        and occurence of various headers has changed over time, even on the
        same instrument. If strict is set to True, the date or time are
        determined from valid FITS keywords. If it cannot be determined, None
        is returned. If dateonly or timeonly are set to True, then a
        datetime.date object or datetime.time object, respectively, is
        returned, containing only the date or time, respectively. These two
        interplay with strict in the sense that if strict is set to True and a
        date can be determined but not a time, then this function will return
        None unless the dateonly flag is set, in which case it will return the
        valid date. The dateonly and timeonly flags are intended for use by
        the ut_date and ut_time descriptors.
        :param dataset: the data set
        :type dataset: AstroData
        :param strict: set to True to not try to guess the date or time
        :type strict: Python boolean
        :param dateonly: set to True to return a datetime.date
        :type dateonly: Python boolean
        :param timeonly: set to True to return a datetime.time
        :param timeonly: Python boolean
        :rtype: datetime.datetime (dateonly=False and timeonly=False)
        :rtype: datetime.time (timeonly=True)
        :rtype: datetime.date (dateonly=True)
        :return: the UT date and time at the start of the observation
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"ut_datetime"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "ut_datetime")
            if not hasattr(self.descriptor_calculator, "ut_datetime"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for ut_datetime"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.ut_datetime(self, **args)
            
            from datetime import datetime
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "ut_datetime",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = datetime )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def ut_time(self, format=None, **args):
        """
        Return the ut_time value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
        :type format: string
        :rtype: datetime as default (i.e., format=None)
        :return: the UT time at the start of the observation
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"ut_time"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "ut_time")
            if not hasattr(self.descriptor_calculator, "ut_time"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for ut_time"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.ut_time(self, **args)
            
            from datetime import datetime
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "ut_time",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = datetime )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def wavefront_sensor(self, format=None, **args):
        """
        Return the wavefront_sensor value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
        :type format: string
        :rtype: string as default (i.e., format=None)
        :return: the wavefront sensor (either 'AOWFS', 'OIWFS', 'PWFS1', 
                 'PWFS2', some combination in alphebetic order separated with 
                 an ampersand or None) used for the observation
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"wavefront_sensor"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "wavefront_sensor")
            if not hasattr(self.descriptor_calculator, "wavefront_sensor"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for wavefront_sensor"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.wavefront_sensor(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "wavefront_sensor",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = str )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def wavelength_reference_pixel(self, format=None, **args):
        """
        Return the wavelength_reference_pixel value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
                       set to as_dict to return a dictionary, where the number 
                       of dictionary elements equals the number of pixel data 
                       extensions in the image. The key of the dictionary is 
                       an (EXTNAME, EXTVER) tuple, if available. Otherwise, 
                       the key is the integer index of the extension.
        :type format: string
        :rtype: float as default (i.e., format=None)
        :rtype: dictionary containing one or more float(s) (format=as_dict)
        :return: the reference pixel of the central wavelength of the 
                 observation
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"wavelength_reference_pixel"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "wavelength_reference_pixel")
            if not hasattr(self.descriptor_calculator, "wavelength_reference_pixel"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for wavelength_reference_pixel"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.wavelength_reference_pixel(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "wavelength_reference_pixel",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = float )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def well_depth_setting(self, format=None, **args):
        """
        Return the well_depth_setting value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
        :type format: string
        :rtype: string as default (i.e., format=None)
        :return: the well depth setting (either 'Shallow', 'Deep' or 
                 'Invalid') of the observation
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"well_depth_setting"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "well_depth_setting")
            if not hasattr(self.descriptor_calculator, "well_depth_setting"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for well_depth_setting"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.well_depth_setting(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "well_depth_setting",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = str )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def x_offset(self, format=None, **args):
        """
        Return the x_offset value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
        :type format: string
        :rtype: float as default (i.e., format=None)
        :return: the x offset of the observation
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"x_offset"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "x_offset")
            if not hasattr(self.descriptor_calculator, "x_offset"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for x_offset"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.x_offset(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "x_offset",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = float )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
    def y_offset(self, format=None, **args):
        """
        Return the y_offset value
        :param dataset: the data set
        :type dataset: AstroData
        :param format: the return format
        :type format: string
        :rtype: float as default (i.e., format=None)
        :return: the y offset of the observation
        """
        try:
            self._lazyloadCalculator()
            keydict = self.descriptor_calculator._specifickey_dict
            key = "key_"+"y_offset"
            #print "mkCI22:",key, repr(keydict)
            #print "mkCI23:", key in keydict
            if key in keydict.keys():
                keyword = keydict[key]
            else:
                keyword = None
            #print hasattr(self.descriptor_calculator, "y_offset")
            if not hasattr(self.descriptor_calculator, "y_offset"):
                if keyword is not None:
                    retval = self.phu_get_key_value(keyword)
                    if retval is None:
                        if hasattr(self, "exception_info"):
                            raise self.exception_info
                else:
                    msg = "Unable to find an appropriate descriptor function "
                    msg += "or a default keyword for y_offset"
                    raise KeyError(msg)
            else:
                retval = self.descriptor_calculator.y_offset(self, **args)
            
            
            ret = DescriptorValue( retval, 
                                   format = format, 
                                   name = "y_offset",
                                   keyword = keyword,
                                   ad = self,
                                   pytype = float )
            return ret
        except:
            if not hasattr(self, "exception_info"):
                setattr(self, "exception_info", sys.exc_info()[1])
            if (self.descriptor_calculator is None 
                or self.descriptor_calculator.throwExceptions == True):
                raise
            else:
                #print "NONE BY EXCEPTION"
                self.exception_info = sys.exc_info()[1]
                return None
    
# UTILITY FUNCTIONS, above are descriptor thunks            
    def _lazyloadCalculator(self, **args):
        '''Function to put at top of all descriptor members
        to ensure the descriptor is loaded.  This way we avoid
        loading it if it is not needed.'''
        if self.descriptor_calculator is None:
            self.descriptor_calculator = Descriptors.get_calculator(self, **args)

