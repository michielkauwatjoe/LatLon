#!/usr/bin/env python3

from setuptools import setup, find_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))

with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name         = 'latlon',
    version      = '1.0.3',
    description  = 'Methods for representing geographic coordinates',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author       = 'Gen Del Raye, Michiel Kauw-A-Tjoe',
    author_email = 'gdelraye@hawaii.edu, michielkauwatjoe@gmail.com',
    url          = '',
    download_url = '',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    keywords     = ['latitude', 'longitude', 'decimal degrees', 'degree minutes', 'distance'],
    setup_requires = ['pyproj'],
    package_data = {},
    licence = 'GPL3',
    classifiers  = [
                  "Intended Audience :: Science/Research",
                  "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
                  "Natural Language :: English",
                  "Operating System :: OS Independent",
                  "Programming Language :: Python",
                  "Topic :: Scientific/Engineering",
                  "Development Status :: 4 - Beta"],
)
