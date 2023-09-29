"""
Recipes available to data with tags ``['GHOST', 'SPECT']``.
Default is ``reduce``. SQ is identical to QA recipe, and is imported
from there.
"""
recipe_tags = set(['GHOST', 'SPECT'])

def reduceScience(p):
    """
    This recipe processes GHOST science data.

    Parameters
    ----------
    p : Primitives object
        A primitive set matching the recipe_tags.
    """

    p.prepare()
    p.addDQ()
    p.addVAR(read_noise=True)
    p.overscanCorrect()
    p.biasCorrect()
    p.ADUToElectrons()
    p.addVAR(poisson_noise=True)
    p.darkCorrect()
    p.tileArrays()
    p.removeScatteredLight()
    p.writeOutputs()
    p.extractProfile()
    p.addWavelengthSolution()  # should be able to accept multiple input
                               # arcs, e.g. from start and end of night,
                               # and interpolate in time
    p.barycentricCorrect()  # trivial - multiply wavelength scale
    p.fluxCalibrate()  # correct for atmospheric extinction before combining
    #p.scaleCountsToReference()  # can be no-op'd with tolerance=0
    p.writeOutputs(suffix="_calibrated", strip=True)  # output these data products
    p.combineOrders()
    p.writeOutputs(suffix="_dragons", strip=True)


def reduceStandard(p):
    """
    This recipe processes GHOST telluric standard data.

    Parameters
    ----------
    p : Primitives object
        A primitive set matching the recipe_tags.
    """

    p.prepare()
    p.addDQ()
    p.addVAR(read_noise=True)
    p.overscanCorrect()
    p.biasCorrect()
    p.ADUToElectrons()
    p.addVAR(poisson_noise=True)
    p.darkCorrect()
    p.tileArrays()
    p.removeScatteredLight()
    p.writeOutputs()
    p.extractProfile()
    p.addWavelengthSolution()
    p.scaleCountsToReference()
    p.stackFrames()
    p.calculateSensitivity()
    p.storeProcessedStandard()


_default = reduceScience
