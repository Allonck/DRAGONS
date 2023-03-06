"""
Recipes available to data with tags ['GNIRS', 'SPECT', LS'].
Default is "reduceScience".
"""
recipe_tags = {'GNIRS', 'SPECT', 'LS'}

def reduceScience(p):
    """
    To be updated as development continues: This recipe processes GNIRS longslit
    spectroscopic data, currently up to basic spectral extraction without telluric correction.

    Parameters
    ----------
    p : :class:`geminidr.gnirs.primitives_gnirs_longslit.GNIRSLongslit`

    """
    p.prepare()
    p.addDQ()
    # p.nonlinearityCorrect() # non-linearity correction tbd
    p.ADUToElectrons()
    p.addVAR(poisson_noise=True, read_noise=True)
    # p.darkCorrect() # no dark correction for GNIRS LS data
    p.flatCorrect()
    p.attachWavelengthSolution()
    p.separateSky()
    p.associateSky()
    p.skyCorrect()
    p.cleanReadout()
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
    Process GNIRS longslist science in order to create wavelength and distortion
    solutions using sky emission lines.

    Inputs are:
      * raw science - no other calibrations required.
    """
    p.prepare()
    p.addDQ()
    p.addVAR(read_noise=True)
    p.ADUToElectrons()
    p.addVAR(poisson_noise=True)
    p.stackFrames()
    p.makeIRAFCompatible()
    p.determineWavelengthSolution()
    p.determineDistortion(debug=True)
    p.storeProcessedArc(force=True)
    p.writeOutputs()

def  makeWavecalFromSkyAbsorption(p):
    """
    Process GNIRS longslist science in order to create wavelength solution
    using telluric absorption in the target spectrum. Copy distortion model
    to the resulting calibration frame from the associated arc.

    Inputs are:
      * raw science
      * processed arc
      * processed flat
    """
    p.prepare()
    p.addDQ()
    # p.nonlinearityCorrect() # non-linearity correction tbd
    p.ADUToElectrons()
    p.addVAR(poisson_noise=True, read_noise=True)
    p.flatCorrect()
    p.attachWavelengthSolution()
    p.writeOutputs()
    p.copyInputs(instream="main", outstream="with_distortion_model")
    p.separateSky()
    p.associateSky()
    p.skyCorrect()
    p.cleanReadout()
    p.distortionCorrect()
    p.findApertures()
    p.determineWavelengthSolution(absorption=True)
    p.transferDistortionModel(source="with_distortion_model")
    p.storeProcessedArc(force=True)

_default = reduceScience
