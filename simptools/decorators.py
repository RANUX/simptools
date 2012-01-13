# -*- coding: UTF-8 -*-
import logging

__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


class catch_and_log_exception(object):

    def __init__(self, return_expression=None):
        """
        If there are decorator arguments, the function
        to be decorated is not passed to the constructor!
        """
        self.return_expressions = return_expression

    def __call__(self, f):
        """
        If there are decorator arguments, __call__() is only called
        once, as part of the decoration process! You can only give
        it a single argument, which is the function object.
        """
        def wrapped_f(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except Exception, e:
                logging.exception(e)
                return self.return_expressions
        return wrapped_f