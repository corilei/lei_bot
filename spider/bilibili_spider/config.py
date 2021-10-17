#!/usr/bin/python
# -*- coding: utf-8 -*-
# Description: 
# Created: lei.cheng 2021/10/12
# Modified: lei.cheng 2021/10/12
import configparser
import os

from spider.bilibili_spider.logger import logger


class Config(object):
    def __init__(self, config_file='config_bili.ini'):
        self._path = os.path.join(os.getcwd(), config_file)
        if not os.path.exists(self._path):
            raise FileNotFoundError("No such file: config_bili.ini")
        self._config = configparser.ConfigParser()
        self._config.read(self._path, encoding='utf-8-sig')
        self._configRaw = configparser.RawConfigParser()
        self._configRaw.read(self._path, encoding='utf-8-sig')

    def get(self, section, name):
        logger.info('加载配置{}下的{}'.format(section, name))
        return self._config.get(section, name)

    def get_raw(self, section, name):
        logger.info('加载配置{}下的{}'.format(section, name))
        return self._configRaw.get(section, name)

    def set(self, section, name, value):
        logger.info('设置配置{}下的{}'.format(section, name))
        self._configRaw.set(section, name, value)


global_config = Config()
