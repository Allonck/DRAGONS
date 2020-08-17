#!/usr/bin/env python
import copy
import os
import itertools
import time

import numpy as np
import pytest
import requests

import astrodata
from astrodata.testing import download_from_archive
from geminidr.core import primitives_visualize
from geminidr.gmos.primitives_gmos_image import GMOSImage
from recipe_system.testing import reduce_arc

test_data = [
    # (Input File, Associated Arc)
    ("N20180112S0209.fits", "N20180112S0353.fits"),
]

HEMI = 'NS'
CCD = ('EEV', 'e2v', 'Ham')


@pytest.mark.parametrize('hemi, ccd', list(itertools.product(HEMI, CCD)))
def test_mosaic_detectors_gmos_binning(hemi, ccd):
    """
    Tests that the spacing between amplifier centres for NxN binned data
    is precisely N times smaller than for unbinned data when run through
    mosaicDetectors()
    """
    astrofaker = pytest.importorskip("astrofaker")

    for binning in (1, 2, 4):
        try:
            ad = astrofaker.create('GMOS-{}'.format(hemi), ['IMAGE', ccd])
        except ValueError:  # No e2v for GMOS-S
            pytest.skip()

        ad.init_default_extensions(binning=binning, overscan=False)
        for ext in ad:
            shape = ext.data.shape
            ext.add_star(amplitude=10000, x=0.5 * (shape[1] - 1),
                         y=0.5 * (shape[0] - 1), fwhm=0.5 * binning)
        p = GMOSImage([ad])
        ad = p.mosaicDetectors([ad])[0]
        ad = p.detectSources([ad])[0]
        x = np.array(sorted(ad[0].OBJCAT['X_IMAGE']))
        if binning == 1:
            unbinned_positions = x
        else:
            diffs = np.diff(unbinned_positions) - binning * np.diff(x)
            assert np.max(abs(diffs)) < 0.01


@pytest.mark.preprocessed_data
@pytest.mark.parametrize("input_ad", test_data, indirect=True)
@pytest.mark.usefixtures("check_adcc")
def test_plot_spectra_for_qa_single_frame(input_ad):
    p = primitives_visualize.Visualize([])
    p.plotSpectraForQA(adinputs=[input_ad])
    assert True


@pytest.mark.preprocessed_data
@pytest.mark.parametrize("input_ad", test_data, indirect=True)
@pytest.mark.usefixtures("check_adcc")
def test_plot_spectra_for_qa_multiple_frames(input_ad):
    """
    Tests that plotSpectraForQA can send single and stacked frames to ADCC. One
    could do this using actual data but it was simply easier to modify a single
    file and send it.

    Parameters
    ----------
    input_ad : fixture
        The input data that will be displayed.
    """

    p_vis = primitives_visualize.Visualize([])
    p_vis.plotSpectraForQA(adinputs=[input_ad])
    time.sleep(5)

    adlist = [input_ad]
    for i in range(1, 3):

        new_ad = copy.deepcopy(input_ad)
        sequence_number = int(input_ad.data_label().split("-")[-1]) + i
        new_data_label = "-".join(input_ad.data_label().split("-")[:-1])
        new_data_label += f"-{sequence_number:03d}"

        new_ad.phu['DATALAB'] = new_data_label
        new_ad[0].data += i * 0.1 * new_ad[0].data.max() * np.random.rand(new_ad[0].data.size)

        p_vis.plotSpectraForQA(adinputs=[new_ad])
        adlist.append(new_ad)
        time.sleep(5)

        p_img = GMOSImage([])
        stack_ad = p_img.stackFrames(adinputs=adlist)[0]
        p_vis.plotSpectraForQA(adinputs=[stack_ad])
        time.sleep(5)



@pytest.fixture(scope='module')
def check_adcc():
    try:
        _ = requests.get(url="http://localhost:8777/rqsite.json")
        print("ADCC is up and running!")
    except requests.exceptions.ConnectionError:
        pytest.skip("ADCC is not running.")


@pytest.fixture(scope='module')
def input_ad(path_to_inputs, request):

    basename, _ = request.param
    input_fname = basename.replace('.fits', '_sensitivityCalculated.fits')
    input_path = os.path.join(path_to_inputs, input_fname)

    if os.path.exists(input_path):
        input_data = astrodata.open(input_path)
    else:
        raise FileNotFoundError(input_path)

    return input_data


def create_inputs():
    """
    Create inputs for `test_plot_spectra_for_qa_single_frame`.

    The raw files will be downloaded and saved inside the path stored in the
    `$DRAGONS_TEST/raw_inputs` directory. Processed files will be stored inside
    a new folder called "dragons_test_inputs". The sub-directory structure
    should reflect the one returned by the `path_to_inputs` fixture.
    """
    import os
    from geminidr.gmos.primitives_gmos_longslit import GMOSLongslit
    from gempy.utils import logutils
    from recipe_system.reduction.coreReduce import Reduce

    path = f"./dragons_test_inputs/geminidr/core/{__file__.split('.')[0]}/"
    os.makedirs(path, exist_ok=True)
    os.chdir(path)
    
    os.makedirs("inputs/")

    for raw_basename, arc_basename in test_data:

        arc_path = download_from_archive(arc_basename)
        raw_path = download_from_archive(raw_basename)
        raw_ad = astrodata.open(raw_path)
        data_label = raw_ad.data_label()

        print('Current working directory:\n    {:s}'.format(os.getcwd()))

        logutils.config(file_name='log_arc_{}.txt'.format(data_label))
        arc_reduce = Reduce()
        arc_reduce.files.extend([arc_path])
        arc_reduce.runr()
        arc_master = arc_reduce.output_filenames.pop()

        logutils.config(file_name='log_{}.txt'.format(data_label))
        p = GMOSLongslit([raw_ad])
        p.prepare()
        p.addDQ(static_bpm=None)
        p.addVAR(read_noise=True)
        p.overscanCorrect()
        p.biasCorrect(do_bias=False)
        p.ADUToElectrons()
        p.addVAR(poisson_noise=True)
        p.flatCorrect(do_flat=False)
        p.QECorrect(arc=arc_master)
        p.distortionCorrect(arc=arc_master)
        p.findSourceApertures(max_apertures=1)
        p.skyCorrectFromSlit()
        p.traceApertures()
        p.extract1DSpectra()
        p.linearizeSpectra()
        # p.calculateSensitivity()

        os.chdir("inputs/")
        print("\n\n    Writing processed files for tests into:\n"
              "    {:s}\n\n".format(os.getcwd()))
        _ = p.writeOutputs()
        os.chdir("../")


if __name__ == "__main__":
    import sys

    if '--create-inputs' in sys.argv[1:]:
        create_inputs()
    else:
        pytest.main()
