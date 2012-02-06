# -*- coding: UTF-8 -*-
import requests


__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


class HttpRequest(object):
    '''
    Here you can put logic for building request.
    '''
    def __init__(self):
        self.GET  = {}
        self.POST = {}

class HttpClientException(Exception):
    pass

class HttpClient(object):
    '''
    Wrapper over requests library.
    For more information over requests
    see https://github.com/kennethreitz/requests/blob/develop/requests/models.py
    '''

    @classmethod
    def execute(cls, request):
        if request.GET:
            return requests.get(**request.GET)
        elif request.POST:
            return requests.post(**request.POST)
        raise HttpClientException("request is empty")
