# -*- coding: UTF-8 -*-
try:
    from django.utils.encoding import smart_unicode
except ImportError:
    smart_unicode = unicode


__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


class DictObject(object):
    '''
    Usage:
    >>> obj=DictObject({ 'a':'1', 'b':'test'}, {'a': {'type': int}})
    >>> obj.a
    >>> obj.b
    '''
    def __init__(self, dict, conversion_rules={}):
        self.conversion_rules = conversion_rules

        for key,value in dict.items():
            if key in conversion_rules:
                validator = conversion_rules[key].get('validator', None)
                if validator:
                    validator(value)
                type = conversion_rules[key].get('type', None)
                if type:
                    value = type(value)
                closure = conversion_rules[key].get('closure', None)
                if closure:
                    value = closure(value)

            self.__dict__.setdefault(key, value)

    def __getattr__(self, attr):
        if attr in self.conversion_rules:
            default_value = self.conversion_rules[attr].get('default', None)
            self.__dict__.setdefault(smart_unicode(attr), default_value)
            return default_value