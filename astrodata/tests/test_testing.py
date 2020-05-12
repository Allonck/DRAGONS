"""
Tests for the `astrodata.testing` module.
"""

import os

import numpy as np
import pytest

import astrodata

from astrodata.testing import assert_same_class, download_from_archive


example_test = """
    from os.path import exists

    def test_cache_file_from_archive_new_file(cache_file_from_archive, capsys):

        filename = 'X20001231S0001.fits'
        path = cache_file_from_archive(filename)
        captured = capsys.readouterr()

        assert "Caching file to:" in captured.out
        assert isinstance(path, str)
        assert filename in path
        assert exists(path)

        _ = cache_file_from_archive(filename)
        captured = capsys.readouterr()
        assert "Input file is cached in:" in captured.out
    """

example_conftest = """
    from astrodata.testing import *

    def pytest_addoption(parser):
            try:
                parser.addoption(
                    "--dragons-remote-data",
                    action="store_true",
                    default=False,
                    help="enable tests that use the cache_file_from_archive fixture"
                )
                parser.addoption(
                    "--force-cache",
                    action="store_true",
                    default=False,
                    help="Forces data cache when using cache_file_from_archive fixture"
                )
                parser.addoption(
                    "--force-preprocess-data",
                    action="store_true",
                    default=False,
                    help="Force preprocessing data as part of the tests."
                )
                parser.addoption(
                    "--do-plots",
                    action="store_true",
                    default=False,
                    help="Plot results of each test after running them."
                )
            # This file is imported several times and might bring conflict
            except ValueError:
                pass
"""


def test_cache_file_from_archive_caching_data(monkeypatch, tmpdir, testdir):
    ncall = 0

    def mock_download(remote_url, **kwargs):
        nonlocal ncall
        ncall += 1
        fname = remote_url.split('/')[-1]
        tmpdir.join(fname).write('')  # create fake file
        return str(tmpdir.join(fname))

    monkeypatch.setattr("astrodata.testing.download_file", mock_download)
    monkeypatch.setenv('DRAGONS_TEST', str(tmpdir))
    testdir.makeconftest(example_conftest)
    testdir.makepyfile(example_test)

    result = testdir.runpytest()
    result.assert_outcomes(skipped=1)
    assert ncall == 0

    result = testdir.runpytest("--dragons-remote-data")
    result.assert_outcomes(failed=1)
    assert ncall == 0

    result = testdir.runpytest("--dragons-remote-data", "--force-cache")
    result.assert_outcomes(passed=1)
    assert ncall == 1


def test_cache_file_from_archive_is_skipped_when_envvar_not_defined(
        monkeypatch, testdir):
    monkeypatch.delenv('DRAGONS_TEST')
    testdir.makeconftest("from astrodata.testing import *")
    testdir.makepyfile(example_test)
    result = testdir.runpytest()
    result.assert_outcomes(skipped=1)


def test_download_from_archive_raises_ValueError_if_envvar_does_not_exists():
    with pytest.raises(ValueError):
        download_from_archive('N20180304S0126.fits', env_var='')


def test_download_from_archive_raises_IOError_if_path_is_not_accessible():
    env_var = 'MY_FAKE_ENV_VAR'
    os.environ['MY_FAKE_ENV_VAR'] = "/not/accessible/path"
    with pytest.raises(IOError):
        download_from_archive('N20180304S0126.fits', env_var=env_var)


def test_download_from_archive(monkeypatch, tmpdir):
    ncall = 0

    def mock_download(remote_url, **kwargs):
        nonlocal ncall
        ncall += 1
        fname = remote_url.split('/')[-1]
        tmpdir.join(fname).write('')  # create fake file
        return str(tmpdir.join(fname))

    monkeypatch.setattr("astrodata.testing.download_file", mock_download)
    monkeypatch.setenv("DRAGONS_TEST", str(tmpdir))

    # first call will use our mock function above
    fname = download_from_archive('N20170529S0168.fits')
    assert os.path.exists(fname)
    assert ncall == 1

    # second call will use the cache so we check that our mock function is not
    # called twice
    fname = download_from_archive('N20170529S0168.fits')
    assert os.path.exists(fname)
    assert ncall == 1


def test_assert_same_class():
    ad = astrodata.create({})
    ad2 = astrodata.create({})
    assert_same_class(ad, ad2)

    with pytest.raises(AssertionError):
        assert_same_class(ad, np.array([1]))
