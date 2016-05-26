#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import numpy as np


@pytest.fixture(scope='function', params=[10, 100, 1000])
def arraydim(request):
    ndim = request.param
    return np.arange(ndim)
