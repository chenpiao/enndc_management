#!/usr/bin/env python
# coding:utf-8
__author__ = 'syx'

import redis


class RedisDatabase:

    def __init__(self):
        self.host = '10.1.201.207'
        self.port = 6379
        self.db = 0

    def get_value(self, key):
        r = redis.Redis(host=self.host, port=self.port, db=self.db)
        data = r.get(key)
        return data


if __name__ == '__main__':
    var = 'ansible_facts10.1.201.47'
    r = RedisDatabase()
    r.get_value(var)
