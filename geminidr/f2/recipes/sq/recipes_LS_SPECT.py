"""
Recipes available to data with tags ['F2', 'SPECT', LS'].
Default is "reduceScience".
"""
recipe_tags = {'F2', 'SPECT', 'LS'}

def reduceScience(p):
    """
    To be updated as development continues: This recipe processes F2 longslit 
    spectroscopic data, currently up to basic extraction (no telluric correction).

    Parameters
    ----------
    p : :class:`geminidr.f2.primitives_f2_longslit.F2Longslit`

    """
    p.prepare()
    p.addDQ()
    p.nonlinearityCorrect() # non-linearity correction tbd even for gemini iraf
    p.ADUToElectrons()
    p.addVAR(poisson_noise=True, read_noise=True)
    p.darkCorrect()
    p.flatCorrect()
    p.attachWavelengthSolution()
    p.separateSky()
    p.associateSky()
    p.skyCorrect()
    p.distortionCorrect()
    p.adjustWCSToReference()
    p.resampleToCommonFrame()
    # p.scaleCountsToReference()
    p.stackFrames()
    p.findApertures()
    p.traceApertures()
    p.storeProcessedScience(suffix="_2D")
    p.extractSpectra()
    p.storeProcessedScience(suffix="_1D")


def  makeWavecalFromSkyEmission(p):
    """
    Process F2 longslist science in order to create wavelength and distortion
    solutions using sky emission lines.

    Inputs are:
       * raw science with caldb requests:
          * procdark with matching exptime
          * procflat
    """

    # Added a temporary workaround for improving distortion model in the frames with
    # large unilluminated areas by using SLITEDGE table from the processed flat
    # for masking the regions beyond the slit into which some lines may be traced.

    #p.selectFromInputs(tags="FLAT", outstream="flat") # temporary workaround
    #p.removeFromInputs(tags="FLAT") # temporary workaround
    p.prepare()
    p.addDQ()
    p.addVAR(read_noise=True)
    p.ADUToElectrons()
    p.addVAR(poisson_noise=True)
    p.darkCorrect()
    #p.transferAttribute(stream="main", source="flat", attribute="SLITEDGE") # temporary workaround
    #p.maskBeyondSlit() # temporary workaround
    p.makeIRAFCompatible()
    p.determineWavelengthSolution()
    p.determineDistortion(debug=True)
    p.storeProcessedArc(force=True)
    p.writeOutputs()
    
_default = reduceScience
