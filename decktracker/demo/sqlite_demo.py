#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""A simple introdution

more description

:Project: https://github.com/JinnCheung/Decktracker
:Author: Jinn Cheung
:Date: 2021/9/27 20:03 
"""
import os
import sqlite3
import subprocess


if __name__ == '__main__':
    # print(sqlite3.version)
    # print(sqlite3.sqlite_version)
    print(os.path.abspath(os.path.dirname(os.getcwd())))
    print(os.path.abspath(os.path.join(os.path.dirname(__file__))))
    print(subprocess.call(["ls", "-l"], shell=False))
    # print(subprocess.call(["sqlite3", "test.db"], shell=False))
