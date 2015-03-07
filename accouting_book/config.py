# -*- coding: utf-8 -*-
class Config(object):
    DEBUG = False
    # cache config
    CACHE_TYPE = 'memcached'
    CACHE_DEFAULT_TIMEOUT = 1800  # 默认缓存30s
    CACHE_KEY_PREFIX = 'card_'  # 所有key之前添加前缀
    CACHE_MEMCACHED_SERVERS = ['127.0.0.1:11211']


class DevelopmentConfig(Config):
    DEBUG = True
