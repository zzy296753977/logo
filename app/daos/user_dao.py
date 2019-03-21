#!/usr/bin/env python
# coding:utf-8
import config
# 数据库地址
db = config.db


class UserDao(object):
    def get_password(self, user_name):
        condition = {'user_name': user_name}
        result = list(db.select('user',condition,what='password',where='user_name =$user_name'))
        if result:
            return result[0].password
        else:
            return None
