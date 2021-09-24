#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import logging
import coloredlogs

log_format = '%(asctime)s - %(levelname)s : %(message)s'

# 1. 配置彩色输出
log = logging.getLogger(name="decktracker")
log.setLevel(logging.getLevelName('DEBUG'))
coloredlogs.install(level='DEBUG', fmt=log_format)

# 2. 配置文件输出???
fileHandler = logging.FileHandler(os.path.join(os.getcwd(), 'debug.log'))
fileHandler.setLevel(logging.getLevelName('INFO'))
fileHandler.setFormatter(logging.Formatter(fmt=log_format, datefmt='%Y-%m-%d %H:%M:%S'))
log.addHandler(fileHandler)
