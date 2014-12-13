#-*- coding:utf-8 -*-

import redis
import cPickle as pickle
import json
import time
from flask import current_app


class RedisCache(object):
    def __init__(self, host='localhost', port=6379, password=None,
                 db=0, default_timeout=None, key_prefix=None):
        self.default_timeout = default_timeout
        self._redis_cliend = redis.Redis(host=host, port=port, password=password, db=db)
        self.key_prefix = key_prefix or ''

    def get(self, key):
        return self._redis_cliend.get(self.key_prefix + key)

    def set(self, key, value, timeout=None):
        if timeout is None:
            timeout = self.default_timeout

        if timeout is not None:
            self._redis_cliend.setex(self.key_prefix + key, value, timeout)
        else:
            self._redis_cliend.set(self.key_prefix + key, value)

    def delete(self, key):
        self._redis_cliend.delete(self.key_prefix + key)

    def inc(self, key, delta=1):
        return self._redis_cliend.incr(self.key_prefix + key, delta)

    def dec(self, key, delta=1):
        return self._redis_cliend.decr(self.key_prefix + key, delta)

    def bulk_delete(self, pattern):
        keys = self._redis_cliend.keys(self.key_prefix + pattern)
        if keys:
            self._redis_cliend.delete(*keys)

    def sadd(self, key, *values):
        return self._redis_cliend.sadd(self.key_prefix + key, *values)

    def srem(self, key, *values):
        return self._redis_cliend.srem(self.key_prefix + key, *values)

    def smembers(self, key):
        return self._redis_cliend.smembers(self.key_prefix + key)

    def scard(self, key):
        return self._redis_cliend.scard(self.key_prefix + key)

    def exists(self, key):
        return self._redis_cliend.exists(self.key_prefix + key)



mc = RedisCache(key_prefix='blog_cache:')


def format_key(key_pattern, **kw):
    keys = key_pattern.split(":")
    keys[1] = kw.get('post_id')
    raw = "{0}:{1}:{2}"
    key = raw.format(*keys)
    return key


def format_post_key(key_pattern, **kw):
    keys = key_pattern.split(":")
    keys[1] = kw.get('post_id')
    raw = "{0}:{1}:{2}"
    key = raw.format(*keys)
    return key


def get_post_cache(cache_key, **kw):
    key_pattern = cache_key.get('key')
    key = format_post_key(key_pattern, **kw)

    current_app.debug_logger.debug('Post Cache Get - %s', key)

    return pickle.loads(mc.get(key))


def set_post_cache(cache_key, **kw):
    key_pattern = cache_key.get('key')
    key = format_post_key(key_pattern, **kw)
    dict_post = {"title": kw.get('post_title'), "content": kw.get('post_content')}

    current_app.debug_logger.debug('Post Cache Set - %s', key)

    return  mc.set(key,pickle.dumps(dict_post))


def get_counter(cache_key, **kw):

    key_pattern = cache_key.get('key')
    key = format_key(key_pattern, **kw)

    return mc.get(key)


def inc_counter(cache_key, delta=1, **kw):
    key_pattern = cache_key.get('key')
    key = format_key(key_pattern, **kw)

    mc.inc(key, delta)


def set_counter(cache_key, value=0, **kw):
    key_pattern = cache_key.get('key')
    key = format_key(key_pattern, **kw)
    current_app.debug_logger.debug('Cache set - %s', key)

    return mc.set(key, value)

# def dec_counter(cache_key, delta=1, **kw):

#     mc.dec(key, delta)
