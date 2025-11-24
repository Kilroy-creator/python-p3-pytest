#!/usr/bin/env python3

from not_none_functions import return_not_none

class TestNotNone:
    '''Tests for not_none_functions.py'''

    def test_return_not_none(self):
        '''function "return_not_none" returns a value that is not None.'''
        assert return_not_none() is not None