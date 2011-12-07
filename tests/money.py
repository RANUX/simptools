# -*- coding: UTF-8 -*-
from decimal import Decimal
from unittest.case import TestCase
import moneyed
from nose.tools import eq_
from simptools.money import Money

__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


class MoneyTests(TestCase):

    def setUp(self):
        self.money = Money(10.0001, moneyed.RUB)

    def test_two_places_round_down(self):
        self.money.round_down()
        eq_(Money('10.00', moneyed.RUB), self.money)

    def test_two_places_round_up(self):
        self.money.round_up()
        eq_(Money('10.01', moneyed.RUB), self.money)