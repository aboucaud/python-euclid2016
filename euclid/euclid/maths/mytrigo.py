#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import numpy as np


def trigo(angle):
    """
    Trigonometry operation that yields 1

    Parameters
    ----------
    angle: int or float
        Input angle

    Returns
    -------
    float

    """
    if angle < 0:
        raise ValueError("Negative angles are not accepted")

    return math.cos(angle)**2 + math.sin(angle)**2


def trigonp(angle):
    """
    Trigonometry vectorial operation that yields 1

    Parameters
    ----------
    angle: `ndarray` of int or float
        Input angles

    Returns
    -------
    `ndarray` of floats

    """
    return np.cos(angle)**2 + np.sin(angle)**2
