# -*- coding: UTF-8 -*-
from decimal import Decimal
from unittest.case import TestCase
from nose.tools import eq_
from simptools.decimals import two_places_round_down, two_places_round_up

__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'

class DecimalsTests(TestCase):

    def setUp(self):
        self.value = 10.0001

    def test_two_places_round_down(self):
        result = two_places_round_down(self.value)
        eq_(Decimal('10.00'), result)

    def test_two_places_round_up(self):
        result = two_places_round_up(self.value)
        eq_(Decimal('10.01'), result)