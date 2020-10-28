#!/usr/bin/env python
# -*- coding: utf-8 -*-


# =============================================================================
# DOCS
# =============================================================================

"""This file is for distribute tinynpydb
"""


# =============================================================================
# IMPORTS
# =============================================================================

import sys
import os
import setuptools

from ez_setup import use_setuptools

use_setuptools()


# =============================================================================
# PATH TO THIS MODULE
# =============================================================================

PATH = os.path.abspath(os.path.dirname(__file__))

# =============================================================================
# Get the version from properimage file itself (not imported)
# =============================================================================

PROPERIMAGE_PY_PATH = os.path.join(PATH, "tinypnpydb.py")

with open(PROPERIMAGE_PY_PATH, "r") as f:
    for line in f:
        if line.startswith("__version__"):
            _, _, TDB_VERSION = line.replace('"', "").split()
            break

# =============================================================================
# REQUIREMENTS
# =============================================================================

REQUIREMENTS = [
    "numpy >= 1.19",
]

# =============================================================================
# DESCRIPTION
# =============================================================================
with open("README.md") as fp:
    LONG_DESCRIPTION = fp.read()

# =============================================================================
# FUNCTIONS
# =============================================================================
print(setuptools.find_packages())  # exclude=['test*']


def do_setup():
    setuptools.setup(
        name="tinynpydb",
        version=TDB_VERSION,
        description="Tiny pickle-based array database",
        long_description=LONG_DESCRIPTION,
        long_description_content_type="text/markdown",
        author="QuatroPE",
        author_email="bruno.sanchez@duke.edu",
        url="https://github.com/quatrope/tinynpydb",
        py_modules=["ez_setup", 'tinynpydb'],
        license="MIT",
        keywords="numpy",
        classifiers=(
            "Development Status :: 4 - Beta",
            "Intended Audience :: Education",
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: Implementation :: CPython",
            "Topic :: Scientific/Engineering",
        ),
        packages=setuptools.find_packages(),  # exclude=['test*']),
        install_requires=REQUIREMENTS,
    )


def do_publish():
    pass


if __name__ == "__main__":
    if sys.argv[-1] == "publish":
        do_publish()
    else:
        do_setup()
