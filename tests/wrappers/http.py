# -*- coding: UTF-8 -*-
import threading
from time import sleep
from unittest.case import TestCase
from nose.tools import eq_, raises
from simptools.wrappers.http import HttpRequest, HttpClient, HttpClientException
from tests.wrappers import server
from tests.wrappers.server import  run_server

__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


class HttpClientTestCase(TestCase):

    SERVER_PORT = 18080

    @classmethod
    def setUpClass(cls):
        cls.server = threading.Thread(target=run_server, kwargs={'port': cls.SERVER_PORT})
        cls.server.setDaemon(True)
        cls.server.start()
        sleep(1)

    def setUp(self):
        self.request = HttpRequest()
        self.data = {
            'url': 'http://localhost:{0}/'.format(self.SERVER_PORT),
        }

    def test_execute(self):
        self.request.GET = self.data
        response = HttpClient.execute(self.request)
        eq_(200, response.status_code)
        self.assertIn(server.TEST_CONTENT, response.text)

    def test_get_request(self):
        self.request.GET = self.data
        self.request.GET.setdefault(
            'params', {
                'a': '1',
                'b': '2',
            }
        )
        response = HttpClient.execute(self.request)
        eq_(200, response.status_code)
        self.assertIn('3', response.text)

    def test_post_request(self):
        self.request.POST = self.data
        self.request.POST.setdefault(
            'data', {
                'a': '1',
                'b': '2',
                }
        )
        response = HttpClient.execute(self.request)
        eq_(200, response.status_code)
        self.assertIn('3', response.text)

    @raises(HttpClientException)
    def test_empty_request(self):
        HttpClient.execute(HttpRequest())

    @classmethod
    def tearDownClass(cls):
        cls.server.join(timeout=1)