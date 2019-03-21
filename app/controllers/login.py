#!/usr/bin/env python
# coding:utf-8
import web
import json
from app.daos.user_dao import UserDao


class Login(object):
    def POST(self):
        web.header('Access-Control-Allow-Origin', '*')
        web.header('Access-Control-Allow-Credentials', 'true')
        result = {}
        # 接受输入
        input_data = web.input(data={})
        # 判断用户存在性
        user_dao = UserDao()
        password = user_dao.get_password(input_data.user_name)
        if password and input_data.password == password :
            result['success'] = True
            return json.dumps(result)
        else:
            result['success'] = False
            return json.dumps(result)

