# Tests for the reduction of echelle flatfield images

import os
import pytest
from numpy.testing import assert_allclose

import pytest_dragons
from pytest_dragons.fixtures import *
from astrodata.testing import ad_compare, download_from_archive

import astrodata, gemini_instruments
from geminidr.ghost.primitives_ghost_bundle import GHOSTBundle
from geminidr.ghost.primitives_ghost_spect import GHOSTSpect
from geminidr.ghost.recipes.sq.recipes_FLAT import makeProcessedFlat
from geminidr.ghost.polyfit.ghost import GhostArm


# flat bundle and root name of processed_bias
datasets = [("S20230513S0463.fits", "S20230513S0439.fits")]


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
@pytest.mark.parametrize("input_filename, bias", datasets,
                         indirect=["input_filename"])
@pytest.mark.parametrize("arm", ("blue", "red"))
def test_reduce_flat(input_filename, bias, arm, path_to_inputs, path_to_refs):
    """Reduce an arm of a flat bundle"""
    adinputs = input_filename[arm]
    processed_bias = os.path.join(
        path_to_inputs, bias.replace(".fits", f"_{arm}001_bias.fits"))
    processed_slitflat = os.path.join(
        path_to_inputs, adinputs[0].phu['ORIGNAME'].split('_')[0]+"_slit_slitflat.fits")
    processed_bpm = os.path.join(
        path_to_inputs, f"bpm_20220601_ghost_{arm}_11_full_4amp.fits")
    ucals = {"processed_bias": processed_bias,
             "processed_slitflat": processed_slitflat,
             "processed_bpm": processed_bpm}
    # A slitflat is needed for both findApertures and measureBlaze
    # and processed_slitflat not recognized as a user_cal
    p = GHOSTSpect(adinputs, ucals=ucals)
    makeProcessedFlat(p)
    assert len(p.streams['main']) == 1
    adout = p.streams['main'].pop()
    output_filename = adout.filename
    adref = astrodata.open(os.path.join(path_to_refs, output_filename))
    assert ad_compare(adref, adout)

    # Comparison doesn't include "exotic" extensions
    assert hasattr(adout[0], "BLAZE")
    assert_allclose(adref[0].BLAZE, adout[0].BLAZE)

    # Need to evaluate XMOD
    arm = GhostArm(arm=adout.arm(), mode=adout.res_mode())
    xmodout = arm.evaluate_poly(adout[0].XMOD)

    # We can reuse the GhostArm object since we already know that 'arm'
    # 'and res_mode' match
    xmodref = arm.evaluate_poly(adref[0].XMOD)
    assert_allclose(xmodref, xmodout)
