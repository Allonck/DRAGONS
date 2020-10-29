#!/usr/bin/env python

"""
Setup script for gemini_python

In this package:
    astrodata
    gemini_instruments
    geminidr
    gempy
    recipe_system

Usage:
    python setup.py install --prefix=/astro/iraf/URlocal-v1.5.2/pkgs/gemini_python-v2.0.0
    python setup.py
"""

import os

from setuptools import setup, find_packages, Extension

from astrodata._version import version

try:
    from Cython.Build import cythonize
except ImportError:
    use_cython = False
else:
    use_cython = True

PACKAGENAME = 'dragons'

PACKAGES = find_packages('.', exclude=['*tests'])

# PACKAGE_DATA
PACKAGE_DATA = {
    'geminidr': ['geminidr/*/lookups/source_detection/*',
                 'geminidr/*/lookups/BPM/*',
                 'geminidr/*/lookups/MDF/*'],
    'gempy': ['gempy/numdisplay/*',
              'gempy/library/config/README'],
    'recipe_system': ['recipe_system/adcc/client/*'],
}

# SCRIPTS
RS_SCRIPTS = [os.path.join('recipe_system', 'scripts', 'adcc'),
              os.path.join('recipe_system', 'scripts', 'caldb'),
              os.path.join('recipe_system', 'scripts', 'reduce'),
              os.path.join('recipe_system', 'scripts', 'superclean'),
              ]

GEMPY_SCRIPTS = [
    os.path.join('gempy', 'scripts', 'dataselect'),
    os.path.join('gempy', 'scripts', 'fwhm_histogram'),
    os.path.join('gempy', 'scripts', 'gmosn_fix_headers'),
    os.path.join('gempy', 'scripts', 'gmoss_fix_HAM_BPMs.py'),
    os.path.join('gempy', 'scripts', 'gmoss_fix_headers.py'),
    os.path.join('gempy', 'scripts', 'pipeline2iraf'),
    os.path.join('gempy', 'scripts', 'profile_all_obj'),
    os.path.join('gempy', 'scripts', 'psf_plot'),
    os.path.join('gempy', 'scripts', 'showrecipes'),
    os.path.join('gempy', 'scripts', 'showd'),
    os.path.join('gempy', 'scripts', 'showpars'),
    os.path.join('gempy', 'scripts', 'swapper'),
    os.path.join('gempy', 'scripts', 'typewalk'),
    os.path.join('gempy', 'scripts', 'zp_histogram'),
]
SCRIPTS = []
SCRIPTS.extend(RS_SCRIPTS)
SCRIPTS.extend(GEMPY_SCRIPTS)

EXTENSIONS = []

if use_cython:
    suffix = 'pyx'
else:
    suffix = 'c'
cyextensions = [Extension(
    "gempy.library.cython_utils",
    [os.path.join('gempy', 'library', 'cython_utils.' + suffix)],
),
]
if use_cython:
    CYTHON_EXTENSIONS = cythonize(cyextensions)
else:
    CYTHON_EXTENSIONS = cyextensions

EXTENSIONS.extend(CYTHON_EXTENSIONS)

setup(name='dragons',
      version=version(),
      description='Gemini Data Processing Python Package',
      author='Gemini Data Processing Software Group',
      author_email='sus_inquiries@gemini.edu',
      url='http://www.gemini.edu',
      maintainer='Science User Support Department',
      license='BSD',
      zip_safe=False,
      packages=PACKAGES,
      package_data=PACKAGE_DATA,
      scripts=SCRIPTS,
      ext_modules=EXTENSIONS,
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Gemini Ops',
          'Intended Audience :: Science/Research',
          'License :: OSI Approved :: BSD License',
          'Operating System :: POSIX :: Linux',
          'Operating System :: Linux :: CentOS',
          'Operating System :: MacOS :: MacOS X',
          'Programming Language :: Python',
          'Topic :: Gemini',
          'Topic :: Data Reduction',
          'Topic :: Scientific/Engineering :: Astronomy',
      ],
      install_requires=[
          'asdf',
          'astropy>=4.1',
          'astroquery',
          'future',
          'ginga',
          'gwcs>=0.14',
          'imexam',
          'matplotlib',
          'numpy',
          'python-dateutil',
          'scipy',
          'specutils',
          'sqlalchemy',
      ],
      extras_require={
          'test': ['pytest', 'pytest-remotedata', 'coverage', 'objgraph'],
      },
      project_urls={
          'Issue Tracker': 'https://github.com/GeminiDRSoftware/DRAGONS',
          'Documentation': 'https://dragons.readthedocs.io/',
      },
      # keywords=['astronomy', 'astrophysics', 'science', 'gemini'],
      python_requires='>=3.6',
      )
