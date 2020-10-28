#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  numpydb.py
#
#  Copyright 2020 QuatroPe
#
# This file is part of ProperImage (https://github.com/quatrope/tinynpydb)
# License: MIT
# Full Text: https://github.com/quatrope/tinynpydb/blob/master/LICENSE
#
import os
import pytest
import tempfile
import pathlib

import numpy as np
import tinynpydb as tnpdb

# =============================================================================
#   CONSTANTS
# =============================================================================
TEMP_DIR = tempfile.mkdtemp(suffix="_tinynpydb")

TEMP_PATH = pathlib.Path(TEMP_DIR)

# =============================================================================
#   FIXTURES
# =============================================================================


@pytest.fixture(scope="session")
def singlearray():
    return np.random.random(size=(3, 3))


@pytest.fixture(scope="session")
def manyarrays():
    return [np.random.random(size=(3, 3)) for i in range(10)]


@pytest.fixture(scope="session")
def staticarray():
    return np.array([[1, 2, 3], [-1, -2, -3], [0.1, 0.2, 0.3]])


# =============================================================================
#   TESTS
# =============================================================================


def test_store_singlearray(singlearray):
    dbname = TEMP_PATH / "test_store_singlearray"
    npdb = tnpdb.NumPyDB(dbname, mode="store")

    assert os.path.exists(dbname.with_suffix(".dat"))
    assert os.path.exists(dbname.with_suffix(".map"))
    assert os.path.isfile(dbname.with_suffix(".dat"))
    assert os.path.isfile(dbname.with_suffix(".map"))

    npdb.dump(singlearray, 0)

    assert len(npdb.positions) == 1


def test_staticarray(staticarray):
    dbname = TEMP_PATH / "test_staticarray"
    npdb = tnpdb.NumPyDB(dbname, mode="store")
    npdb.dump(staticarray, 0)

    assert len(npdb.positions) == 1

    npdb2 = tnpdb.NumPyDB(dbname, mode="load")
    loaded_array, loaded_id = npdb2.load(0)

    np.testing.assert_array_equal(staticarray, loaded_array)


def test_store_manyarrays(manyarrays):
    dbname = TEMP_PATH / "test_store_manyarrays"
    npdb = tnpdb.NumPyDB(dbname, mode="store")

    for iarray, anarray in enumerate(manyarrays):
        npdb.dump(anarray, iarray)

    assert len(npdb.positions) == len(manyarrays)


def test_load_manyarrays(manyarrays):
    original_arrays = manyarrays
    dbname = TEMP_PATH / "test_load_manyarrays"
    npdb = tnpdb.NumPyDB(dbname, mode="store")

    for iarray, anarray in enumerate(original_arrays):
        npdb.dump(anarray, iarray)

    npdb2 = tnpdb.NumPyDB(dbname, mode="load")
    for iarray, anarray in enumerate(original_arrays):
        loaded_array, loaded_id = npdb2.load(iarray)
        assert str(iarray) == loaded_id
        np.testing.assert_array_equal(original_arrays[iarray], loaded_array)


# =============================================================================
#   TESTING EXCEPTIONS
# =============================================================================


def test_opening_nonexisting_db():
    dbname = TEMP_PATH / "test_opening_nonexisting_db"

    with pytest.raises(IOError):
        tnpdb.NumPyDB(dbname, mode="load")


def test_bad_identifier(manyarrays):
    dbname = TEMP_PATH / "test_bad_identifier"
    npdb = tnpdb.NumPyDB(dbname, mode="store")

    for iarray, anarray in enumerate(manyarrays):
        npdb.dump(anarray, iarray)

    with pytest.raises(LookupError):
        npdb.load(42)
