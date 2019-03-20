#!/usr/bin/env python
# coding:utf-8

import web


urls = (
  '/test', 'app.controllers.test.test'
)
app = web.application(urls, globals())
if __name__=="__main__":
    #web.wsgi.runwsgi = lambda func, addr=None: web.wsgi.runfcgi(func, addr)
    app.run()