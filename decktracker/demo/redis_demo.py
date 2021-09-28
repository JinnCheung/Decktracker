#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""A simple introdution

more description

:Project: https://github.com/JinnCheung/Decktracker
:Author: Jinn Cheung
:Date: 2021/9/28 08:36 
"""
import time
import pickle
from datetime import datetime as dt
from functools import wraps
from redis import StrictRedis

from decktracker.log import log


class Cache(object):
    """Redis缓存装饰类"""

    def __init__(self, expire=0.0, life=3600.0):
        """初始化缓存
        @param expire 是截止时间, 默认为0
        @param life 是保存时长, 默认为3600秒
        """
        # 如设置了expire，使用expire，如设置了life，通过life计算expire
        self.expire = expire if bool(expire) else time.time() + life

        try:
            self.redis = StrictRedis(host='localhost', port=6379, db=0)
            self.redis.client_list()
            self.redis_connected = True
            # log.debug("Redis已链接.")
        except Exception as e:
            self.redis_connected = False
            log.error("Redis问题: %s" % e.args[0])

    def save_redis(self, key, value):
        if self.redis_connected:
            log.debug('将[%s]数据保存到redis.' % key)
            if self.expire > 0:
                self.redis.set(key, pickle.dumps(value), ex=int(self.expire - time.time()))
            else:
                self.redis.set(key, pickle.dumps(value))

    def load_redis(self, key):
        if self.redis_connected:
            if self.redis.ttl(key) < 0:
                ttl = '永久有效'
            else:
                ttl = '[%s]过期' % dt.fromtimestamp(time.time() + self.redis.ttl(key)).strftime('%Y-%m-%d %H:%M:%S')
            log.debug("从Redis缓存载入[%s], %s." % (key, ttl))
            return pickle.loads(self.redis.get(key))

    def clear_redis(self, key=''):
        if self.redis_connected:
            if key == '':
                for k in self.redis.keys():
                    self.redis.delete(k)
                log.info('redis remove all keys')
            else:
                log.info('redis remove [%s] %s' % (key, 'success' if bool(self.redis.delete(key)) else 'fail'))

    def list_all_redis(self):
        if self.redis_connected:
            for k in self.redis.keys():
                log.debug("Redis中存在的键%s" % k)

    def __call__(self, func):
        @wraps(func)
        def wrapped_function(*args, **kwargs):

            # === 函数名+参数转换为键名 ===
            args_s = "_".join(["%s" % v for v in args]) if len(args) > 0 else ''
            kwargs_s = "_".join(["%s" % v for k, v in kwargs.items()]) if len(kwargs) > 0 else ''
            key = "%s_%s" % (func.__name__, args_s) if len(args_s) > 0 else func.__name__
            key = "%s_%s" % (key, kwargs_s) if len(kwargs_s) > 0 else key

            if self.redis_connected:

                # === 从redis载入数据 ===
                if self.redis.exists(key):
                    result = self.load_redis(key)
                else:
                    result = func(*args, **kwargs)
                    self.save_redis(key, result)
            else:
                log.error("Redis未连接.")
                result = func(*args, **kwargs)

            return result

        return wrapped_function


@Cache()
def test2(col1, col2):
    return "fuck you %s %s " % (col1, col2)


if __name__ == '__main__':
    # print(test2('col1', 'col2'))
    c = Cache()
    c.save_redis("fuck", "you")
    c.load_redis("fuck")
    c.clear_redis()
    pass
