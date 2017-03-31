# -*- coding: utf-8 -*-
###########################################
import time

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    param = environ['PATH_INFO'][1:] or 'web'
    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    return [('<h1>Hello, %s! <p/> Time: %s</h1>' % (param, t)).encode()]
