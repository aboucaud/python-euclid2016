#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import numpy as np

from numpy.testing import assert_almost_equal

from euclid.maths import trigo, trigonp


def test_trigo_simple():
    """
    The simplest test:

    assert <condition that should be met>

    """
    assert trigo(10) == 1


def test_trigo_simple_fail():
    """
    Catching a specific Exception

    with pytest.raises(Exception):
        <call that should raise the exception>

    """
    with pytest.raises(ValueError):
        trigo(-40)


def test_trigonp_simple(simplearray):
    """
    Using a simple fixture from the conftest.py file.
    The fixture to be used in the test should be given as argument
    of the test: here a basic numpy array
    The fixture is then called during the test.

    It avoids hardcoding the same array for every test.

    In this specific test, since the equality test "==" on numpy arrays
    returns an array of booleans, one must check that all the elements
    are `True` with the np.all() method.

    However due to floating point errors in the calculation of trigonp,
    the returned values are not always equal to one. Thus the use
    np.allclose() allows for some tiny departure around the checked
    value.

    """
    assert np.allclose(trigonp(simplearray),
                       np.ones_like(simplearray, dtype=float))


def test_trigonp_size(arraysize):
    """
    This time, the fixture `arraysize` takes several parameters in input
    (see conftest.py)
    This means that every test using the fixture will be run for every
    parameter of the fixture.
    In this case the test will be on arrays with different size.

    Moreover, we introduce here test triggers provided in the
    `numpy.testing` submodule.
    The various numpy assert methods can be parametrized in many ways to
    ensure both the precision and the accuracy of the tests.

    """
    assert_almost_equal(trigonp(arraysize),
                        np.ones_like(arraysize, dtype=float))


def test_trigonp_dtype(simplearray, dtypes):
    """
    Various fixtures can be used for a given test. Again they need
    to be mentioned as arguments of the tests.

    Here we test the method on the `simplearray` and different data
    types `dtypes`.

    """
    assert_almost_equal(trigonp(simplearray),
                        np.ones_like(simplearray, dtype=dtypes))


def test_trigonp_dim_and_dtype(arraysize, dtypes):
    """
    In the specific case where several fixtures are parametrized, the
    a single test will be run for each combination of the full parameter
    set.

    Here we test both the array size and the data type, and for each
    size of array, all data types will be tested, that is
    3 size x 4 dtype = 12 combinations

    """
    assert_almost_equal(trigonp(arraysize),
                        np.ones_like(arraysize, dtype=dtypes))
