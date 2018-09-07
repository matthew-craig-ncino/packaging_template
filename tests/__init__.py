# -*- coding: utf-8 -*-

"""Unit test package for package_template."""
import unittest
# Notice the "." it makes it work in python2 & python3
from .test_package_template import TestPackage_template


def my_module_suite():
    loader = unittest.TestLoader()
    suite = loader.discover('tests', pattern='test_*.py')
    return suite
