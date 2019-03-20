#!/usr/bin/env python
# coding:utf-8
import web
import json

class test:
    def GET(self):
        web.header('Access-Control-Allow-Origin', '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        result = {}
        result['success'] = True
        return json.dumps(result)