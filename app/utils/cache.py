#-*- coding:utf-8 -*-


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
