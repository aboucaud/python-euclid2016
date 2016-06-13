#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np


def average(array):
    """
    Stupid method that returns the average value of an array

    Parameters
    ----------
    array: `numpy.ndarray` or list
        Array of values

    Returns
    -------
    float

    """
    arr = np.asarray(array, dtype=float)
    return np.mean(arr)
