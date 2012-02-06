# -*- coding: UTF-8 -*-
from optparse import OptionParser
import os
from flask import Flask
from flask import request

app = Flask(__name__)


__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'

TEST_CONTENT = "Hello World!"
PATH_TO_SERVER = os.path.realpath(__file__)

def sum(a, b):
    return '{0}'.format(int(a) + int(b))


@app.route("/", methods=['GET', 'POST'])
def index():
    response = TEST_CONTENT

    if request.method == 'GET':
        a = request.args.get('a', '')
        b = request.args.get('b', '')
        if a and b:
            response = sum(a, b)

    if request.method == 'POST':
        a = request.form['a']
        b = request.form['b']
        response = sum(a, b)

    return response

def run_server(*args, **kwargs):
    app.run(*args, **kwargs)

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('--host',  default='127.0.0.1')
    parser.add_option('--port', type="int", default=5000)

    (options, args) = parser.parse_args()

    app.run(host=options.host, port=options.port)