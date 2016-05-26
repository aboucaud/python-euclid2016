#!/usr/bin/env python
# -*- coding: utf-8 -*-

from time import strftime, gmtime

__all__ = ['now']


def now():
    """
    Print the current time in a readable way
    """
    print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
