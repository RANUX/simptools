# -*- coding: UTF-8 -*-
import logging

__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


def catch_and_log_exception(function=None):
    def decorator(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except Exception, e:
            logging.exception(e)
    return decorator