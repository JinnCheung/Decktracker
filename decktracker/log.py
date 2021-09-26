#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Print colored log on commandline/debug.log .

For example:

>>> from decktracker.log import log

>>> log.debug("here some debug info")
2021-09-25 07:20:19 - DEBUG : here some debug info

>>> log.error("here some error info")
2021-09-25 07:31:38 - ERROR : here some error info

:Project: https://github.com/JinnCheung/Decktracker
:Author: Jinn Cheung
:Date: 2021/9/25 07:10
"""

import os
import logging
import coloredlogs

log = logging.getLogger(name="decktracker")

log.setLevel(logging.getLevelName('DEBUG'))

log_format = '%(asctime)s - %(levelname)s : %(message)s'
coloredlogs.install(level='DEBUG', fmt=log_format)

fileHandler = logging.FileHandler(os.path.join(os.getcwd(), 'debug.log'))
fileHandler.setLevel(logging.getLevelName('INFO'))
fileHandler.setFormatter(logging.Formatter(fmt=log_format, datefmt='%Y-%m-%d %H:%M:%S'))

log.addHandler(fileHandler)
