# Tests for the reduction of echelle bias images

import os
import pytest

import pytest_dragons
from pytest_dragons.fixtures import *
from astrodata.testing import ad_compare, download_from_archive

import astrodata, gemini_instruments
from geminidr.ghost.primitives_ghost_bundle import GHOSTBundle
from geminidr.ghost.primitives_ghost_spect import GHOSTSpect
from geminidr.ghost.recipes.sq.recipes_BIAS import makeProcessedBias


datasets = ["S20230513S0439.fits"]


@pytest.fixture
def input_filename(request):
    ad = astrodata.open(download_from_archive(request.param))
    p = GHOSTBundle([ad])
    adoutputs = p.splitBundle()
    return_dict = {}
    for arm in ("blue", "red"):
        return_dict[arm] = [ad for ad in adoutputs if arm.upper() in ad.tags]
    return return_dict


@pytest.mark.dragons_remote_data
@pytest.mark.integration_test
@pytest.mark.ghost
@pytest.mark.parametrize("input_filename", datasets, indirect=True)
@pytest.mark.parametrize("arm", ("blue", "red"))
def test_reduce_bias(input_filename, arm, path_to_refs):
    """Reduce an arm of a bias bundle"""
    adinputs = input_filename[arm]
    p = GHOSTSpect(adinputs)
    makeProcessedBias(p)
    assert len(p.streams['main']) == 1
    adout = p.streams['main'].pop()
    output_filename = adout.filename
    adref = astrodata.open(os.path.join(path_to_refs, output_filename))
    assert ad_compare(adref, adout, ignore_kw=['PROCBIAS'])
