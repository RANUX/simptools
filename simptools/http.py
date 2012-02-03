# -*- coding: UTF-8 -*-
import requests


__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


class HttpRequest(object):

    def __init__(self):
        self.GET  = {}
        self.POST = {}

class HttpClient(object):
    '''
    Wrapper over requests library
    '''

    @classmethod
    def execute(cls, request):
        if request.GET:
            return requests.get(**request.GET)
        elif request.POST:
            return requests.post(**request.POST)
        return None
