import tornado.wsgi
import wsgiref.simple_server
import os

from server import application

ip = os.environ['OPENSHIFT_PYTHON_IP']
port = int(os.environ['OPENSHIFT_PYTHON_PORT'])

wsgi_app = tornado.wsgi.WSGIAdapter(application)
server = wsgiref.simple_server.make_server(ip, port, wsgi_app)
server.serve_forever()

