from wsgiref.simple_server import make_server

def application(environ,start_response):
    headers = [('content-type','text/plain; charset=utf-8')]

    start_response('200 OK',headers)

    return ['Hello world'.encode('utf-8')]

server = make_server('localhost',8000,application)
server.serve_forever()
