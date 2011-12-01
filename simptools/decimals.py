# -*- coding: UTF-8 -*-
from decimal import Decimal, ROUND_DOWN, ROUND_UP

__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


def two_places_round_down(value):
    return Decimal(value).quantize(Decimal('0.01'), rounding=ROUND_DOWN)

def two_places_round_up(value):
    return Decimal(value).quantize(Decimal('0.01'), rounding=ROUND_UP)