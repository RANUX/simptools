# -*- coding: UTF-8 -*-
from unittest.case import TestCase
from nose.tools import raises
from simptools.classes import class_factory


__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


class EmptyClass():
    pass


class ClassFactoryTests(TestCase):

    def test_dynamical_class_loading(self):
        EmptyClass = class_factory('tests.classes.EmptyClass')
        empty_cls = EmptyClass()
        self.assertIsInstance(empty_cls, EmptyClass)

    @raises(AttributeError)
    def test_try_load_unexist_class(self):
        unexist = class_factory('Unexist')

