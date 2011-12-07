# -*- coding: UTF-8 -*-
from decimal import Decimal, ROUND_UP, ROUND_DOWN
from moneyed.classes import Money


__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


'''
moneyed.Money extension
'''
def round_up(money):
    return Money(Decimal(money.amount).quantize(Decimal('0.01'), rounding=ROUND_UP), money.currency)

def round_down(money):
    return Money(Decimal(money.amount).quantize(Decimal('0.01'), rounding=ROUND_DOWN), money.currency)
