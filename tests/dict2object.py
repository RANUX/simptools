# -*- coding: UTF-8 -*-
import re
from unittest.case import TestCase
from nose.tools import eq_, raises
from simptools.dict2object import DictObject


__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'



class DictObjectTests(TestCase):

    def setUp(self):
        self.data={'int_value': '1', 'str_value': 'test', 'float_value': '23.8'}

    def test_conversion_without_rules(self):
        dobj = DictObject(self.data)
        eq_(dobj.int_value, self.data['int_value'])
        eq_(dobj.str_value, self.data['str_value'])
        eq_(dobj.float_value, self.data['float_value'])

    def test_type_conversion(self):
        dobj = DictObject(self.data, {'int_value': {'type': int},
                                      'str_value': {},
                                      'float_value': {'type': float}})
        self.assertCovertedDataDictEqualsToDictObject(dobj)

    @raises(Exception)
    def test_invalid_conversion(self):

        class RegexValidator(value):
            def __init__(self, regex):
                self.regex = regex

            def __call__(self, value):
                if not self.regex.search(unicode(value)):
                    raise Exception

        dobj = DictObject(self.data, {'int_value': { 'validator': RegexValidator(re.compile('^[3-9]+$'))}})

    def test_unexistent_values(self):
        dobj = DictObject(self.data, {'int_value': {'type': int},
                                      'str_value': {},
                                      'float_value': {'type': float},
                                      'unexistent1': {'default': 100},
                                      'unexistent2': {'default': 200}})
        self.assertCovertedDataDictEqualsToDictObject(dobj)
        eq_(dobj.unexistent1, 100)
        eq_(dobj.unexistent2, 200)

    def test_unexistent_without_default_value(self):
        dobj = DictObject(self.data, {'int_value': {'type': int},
                                      'str_value': {},
                                      'float_value': {'type': float},
                                      'unexistent': {}})
        eq_(dobj.unexistent, None)

    def test_apply_closure_to_value(self):
        dobj = DictObject(self.data, {'int_value': {'type': int,
                                      'closure': lambda value: max(value, 100)},
                                      'str_value': {},
                                      'float_value': {'type': float}})
        eq_(dobj.int_value, 100)

    def assertCovertedDataDictEqualsToDictObject(self, dobj):
        eq_(dobj.int_value, int(self.data['int_value']))
        eq_(dobj.str_value, self.data['str_value'])
        eq_(dobj.float_value, float(self.data['float_value']))

