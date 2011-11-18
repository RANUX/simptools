# -*- coding: UTF-8 -*-
__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'

def class_factory(path):
    modules_names = path.split('.')
    class_name = modules_names.pop()
    module = __import__('.'.join(modules_names), globals(), locals(), [class_name])
    cls = getattr(module, class_name)
    return cls