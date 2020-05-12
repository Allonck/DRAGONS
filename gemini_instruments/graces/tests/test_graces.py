import pytest

import astrodata
import astrodata.testing
import gemini_instruments

filename = 'N20190116G0054i.fits'


@pytest.fixture
def ad():
    path = astrodata.testing.download_from_archive(filename)
    return astrodata.open(path)


@pytest.mark.xfail(reason="AstroFaker changes the AstroData factory")
def test_is_right_type(ad):
    assert type(ad) == gemini_instruments.graces.adclass.AstroDataGraces


def test_is_right_instance(ad):
    # YES, this *can* be different from test_is_right_type. Metaclasses!
    assert isinstance(ad, gemini_instruments.graces.adclass.AstroDataGraces)


def test_extension_data_shape(ad):
    data = ad[0].data
    assert data.shape == (28, 190747)


def test_tags(ad):
    tags = ad.tags
    expected = {'UNPREPARED', 'RAW', 'SPECT', 'GEMINI', 'GRACES'}
    assert expected.issubset(tags)


def test_can_return_instrument(ad):
    assert ad.phu['INSTRUME'] == 'GRACES'
    assert ad.instrument() == ad.phu['INSTRUME']


def test_can_return_ad_length(ad):
    assert len(ad) == 1


def test_slice_range(ad):
    metadata = ('SCI', 2), ('SCI', 3)
    slc = ad[1:]

    assert len(slc) == 0

    for ext, md in zip(slc, metadata):
        assert (ext.hdr['EXTNAME'], ext.hdr['EXTVER']) == md


def test_read_a_keyword_from_hdr(ad):
    try:
        assert ad.hdr['CCDNAME'] == 'GRACES'
    except KeyError:
        # KeyError only accepted if it's because headers out of range
        assert len(ad) == 1
