# -*- coding: UTF-8 -*-
from decimal import Decimal, ROUND_UP, ROUND_DOWN
import moneyed


__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


class Money(moneyed.Money):
    '''
    moneyed.Money extension
    '''
    def round_up(self):
        self.amount = Decimal(self.amount).quantize(Decimal('0.01'), rounding=ROUND_UP)

    def round_down(self):
        self.amount = Decimal(self.amount).quantize(Decimal('0.01'), rounding=ROUND_DOWN)
