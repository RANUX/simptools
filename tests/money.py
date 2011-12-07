# -*- coding: UTF-8 -*-
from decimal import Decimal
from unittest.case import TestCase
import moneyed
from nose.tools import eq_
from simptools.money import Money, round_down, round_up

__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


class MoneyTests(TestCase):

    def setUp(self):
        self.money = Money(10.0001, moneyed.RUB)

    def test_two_places_round_down(self):
        result = round_down(self.money)
        eq_(Money('10.00', moneyed.RUB), result)

    def test_two_places_round_up(self):
        result = round_up(self.money)
        eq_(Money('10.01', moneyed.RUB), result)