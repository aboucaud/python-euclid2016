#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import numpy as np


@pytest.fixture
def simplearray():
    """
    Basic fixture: a simple numpy array for general testing purposes
    """
    return np.array([1, 2, 3])


@pytest.fixture(params=[10, 100, 1000])
def arraysize(request):
    """
    Parametrized fixture: a numpy array with a varying size

    The parameters should be set as a list under the `params` keyword

    Then in the fixture definition, the `request` argument must be used
    in order to retrieve the parameters

    """
    return np.arange(request.param)


@pytest.fixture(params=[np.int32, np.int64, np.float32, np.float64])
def dtypes(request):
    """
    Parametrized fixture: returns numpy data types

    More information on fixtures can be found on
    http://pytest.org/latest/fixture.html
    and
    http://pytest.org/latest/builtin.html#_pytest.python.fixture

    """
    return request.param
