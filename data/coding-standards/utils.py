#!/usr/bin/env python
# Copyright (C) 2012-2020 Euclid Science Ground Segment
#
# This library is free software; you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation; either version 3.0 of the License, or (at your option)
# any later version.
#
# This library is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this library; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA

"""
this is a module that provides some exception error classes
"""

import os
import fcntl


class Lock(object):
    """This is a lock class"""
    def __init__(self, path):
        """can raise IOError, throws IOError"""
        self._lock_file = os.open(path, os.O_RDWR | os.O_CREAT)
        # can raise IOError
        fcntl.lockf(self._lock_file, fcntl.LOCK_EX)

    def unlock(self):
        """can raise IOError, throws IOError"""
        fcntl.lockf(self._lock_file, fcntl.LOCK_UN)
        os.close(self._lock_file)

    # def __del__(self): #throws IOError
    #     # can raise IOError
    #     fcntl.lockf(self._lock_file, fcntl.LOCK_UN)
    #     os.close(self._lock_file)


class SubmissionError(Exception):
    """this is an error class"""
    def __init__(self, s=-1):
        super(SubmissionError, self).__init__()
        self.msg = s

    def __str__(self):
        return "qsub returned " + self.msg


class JobRunningError(Exception):
    """this is an another error class"""
    def __str__(self):
        return "cannot return exit status of a running job"


class InvalidConfigError(Exception):
    """this is an yet another error class"""
    def __init__(self, s=""):
        super(InvalidConfigError, self).__init__()
        self.msg = s

    def __str__(self):
        return "[InvalidConfigurationError] " + self.msg


class InvalidInputFile(Exception):
    """... and another error class"""
    def __init__(self, msg=""):
        super(InvalidInputFile, self).__init__()
        self.msg = msg

    def __str__(self):
        return self.msg
