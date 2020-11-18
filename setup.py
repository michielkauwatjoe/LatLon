from setuptools import setup

setup(
      name         = 'LatLon',
      packages     = ['latlon'],
      version      = '1.0.2',
      description  = 'Methods for representing geographic coordinates',
      author       = 'Gen Del Raye',
      author_email = 'gdelraye@hawaii.edu',
      url          = '',
      download_url = '',
      keywords     = ['latitude', 'longitude', 'decimal degrees', 'degree minutes', 'distance'],
      install_requires = ['pyproj'],
      package_data = {},
      classifiers  = [
                      "Intended Audience :: Science/Research",
                      "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
                      "Natural Language :: English",
                      "Operating System :: OS Independent",
                      "Programming Language :: Python",
                      "Topic :: Scientific/Engineering",
                      "Development Status :: 4 - Beta"],
      )
