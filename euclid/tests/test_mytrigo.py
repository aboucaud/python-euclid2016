#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import numpy as np

from euclid.maths.mytrigo import trigo, trigonp


def test_trigo_simple():
    assert trigo(10) == 1


def test_trigo_array(arraydim):
    assert np.allclose(trigonp(arraydim), np.ones_like(arraydim, dtype=float))


def test_trigo_ndim(arraydim):
    assert trigonp(arraydim).shape == arraydim.shape


def test_trigo_negative():
    """
    For a good coverage, it is important
    to also test the expected failures of
    the program.
    """
    with pytest.raises(ValueError):
        trigo(-1)
