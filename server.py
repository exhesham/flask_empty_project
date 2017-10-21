'''
The MIT License (MIT)

Copyright (c) 2017 Thunderclouding.com - exhesham

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''



import os
from flask import Flask
from flask import make_response
from flask import render_template
from flask import send_from_directory
import ConfigParser

app = Flask(__name__)
dir_path = os.path.dirname(os.path.realpath(__file__))

config = ConfigParser.ConfigParser()
config.readfp(open('config.ini'))


@app.errorhandler(500)
def handle_internal_server_error(e):
    return render_template('err500.html'), 500

@app.route('/favicon.ico')
def favicon():
    print "favicon from ",app.root_path
    return send_from_directory(os.path.join(app.root_path, 'templates'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/<name>')
@app.route('/')
def main_template(name=None):
    print name
    if not name:
        name = 'index.html'

    return make_response(os.path.join(app.root_path, 'templates', name).read())

if __name__ == '__main__':

    app.run(debug=True, port=config.getint('server', 'port'),
            host=config.get('server', 'host'),
            ssl_context=(config.get('server', 'cert_path'),
                         config.get('server', 'cert_key_path')),  threaded=True)
