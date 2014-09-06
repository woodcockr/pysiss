#!/usr/bin/env python
""" file: setup.pyb (pysiss.borehole)
    author: Jess Robertson, CSIRO Earth Science and Resource Engineering
    date: Wednesday 1 May, 2013

    description: Distutils installer script for pysiss.borehole.
"""

import distribute_setup
distribute_setup.use_setuptools()
from setuptools import setup, find_packages

with open('requirements.txt', 'rb') as fhandle:
	REQUIREMENTS = fhandle.read()

## PACKAGE INFORMATION
setup(
    name='pysiss',
    version='0.0.2',
    description='A pythonic interface to Spatial Information Services Stack '
                '(SISS) services',
    long_description=open('README.rst').read(),
    author='Jess Robertson',
    author_email='jesse.robertson@csiro.au',
    url='http://github.com/pysiss/pysiss',
    packages=find_packages(),
    package_data={
        'pysiss.vocabulary.resources': ['*']
    },
    install_requires=REQUIREMENTS,
    test_suite='tests',
    ext_modules=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2 :: Only',
        'Topic :: Internet',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: GIS',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Markup :: XML'
    ]
)
