"""
Recipes available to data with tags ['NIRI', 'SPECT', LS'].
Default is "reduceScience".
"""
recipe_tags = {'NIRI', 'SPECT', 'LS'}

def reduceScience(p):
    """
    To be updated as development continues: This recipe processes NIRI longslit
    spectroscopic data, currently up to a basic spectral extraction without telluric correction.

    Parameters
    ----------
    p : :class:`geminidr.niri.primitives_niri_longslit.NIRILongslit`

    """
    p.prepare()
    p.addDQ()
    p.ADUToElectrons()
    p.addVAR(poisson_noise=True, read_noise=True)
    p.nonlinearityCorrect()
    # p.darkCorrect() # no dark correction for NIRI LS data
    p.flatCorrect()
    p.attachWavelengthSolution()
    p.adjustWavelengthZeroPoint()
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
    Process NIRI longslist science in order to create wavelength and distortion
    solutions using sky emission lines.

    Inputs are:
      * raw science - no other calibrations required.
    """

    # Added p.flatCorrect with a new parameter "rectify" set to "False" as a temporary
    # workaround for improving distortion model in the frames with
    # large unilluminated areas by masking the regions beyond the slit into which
    # some lines may be traced.

    p.prepare()
    p.addDQ()
    p.addVAR(read_noise=True)
    p.ADUToElectrons()
    p.addVAR(poisson_noise=True)
    p.nonlinearityCorrect()
    p.flatCorrect(rectify=False) # temporary workaround
    p.writeOutputs()
    p.stackFrames()
    p.makeIRAFCompatible()
    p.determineWavelengthSolution()
    p.cleanReadout()
    p.determineDistortion(debug=True)
    p.storeProcessedArc(force=True)
    p.writeOutputs()

def  makeWavecalFromSkyAbsorption(p):
    """
    Process NIRI longslist science in order to create wavelength solution
    using telluric absorption in the target spectrum. Copy distortion model
    to the resulting calibration frame from the associated arc.

    Inputs are:
      * raw science
      * processed arc
      * processed flat
    """
    p.prepare()
    p.addDQ()
    p.nonlinearityCorrect()
    p.ADUToElectrons()
    p.addVAR(poisson_noise=True, read_noise=True)
    p.flatCorrect()
    p.attachWavelengthSolution()
    p.copyInputs(instream="main", outstream="with_distortion_model")
    p.separateSky()
    p.associateSky()
    p.skyCorrect()
    p.cleanReadout()
    p.distortionCorrect()
    p.adjustWCSToReference()
    p.resampleToCommonFrame(force_linear=False)
    p.scaleCountsToReference()
    p.stackFrames()
    p.findApertures()
    p.determineWavelengthSolution(absorption=True)
    p.transferDistortionModel(source="with_distortion_model")
    p.storeProcessedArc(force=True)


_default = reduceScience
