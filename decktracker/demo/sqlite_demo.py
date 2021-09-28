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
from toml_demo import data_folder


def create_table():
    # 连接到SQLite数据库
    # 如果文件不存在，会自动创建:
    conn = sqlite3.connect(os.path.join(data_folder, 'test.db'))

    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE user4(id INTEGER PRIMARY KEY, name VARCHAR(20))")


def insert_row():
    # 连接到SQLite数据库
    # 如果文件不存在，会自动创建:
    conn = sqlite3.connect(os.path.join(data_folder, 'test.db'))
    with conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO user4(name) VALUES('Jinn Cheung')")
        print(cur.lastrowid)


def query():
    # 连接到SQLite数据库
    # 如果文件不存在，会自动创建:
    conn = sqlite3.connect(os.path.join(data_folder, 'test.db'))
    with conn:
        cur = conn.cursor()
        cur.execute('SELECT SQLITE_VERSION()')

        data = cur.fetchone()[0]

        print("SQLite version: %s" % data)

        cur.execute('SELECT * FROM user4')

        for row in cur.fetchall():
            print("%s %s" % (row[0], row[1]))


if __name__ == '__main__':
    # print(sqlite3.version)
    # print(sqlite3.sqlite_version)
    # print(os.path.abspath(os.path.dirname(os.getcwd())))
    # print(os.path.abspath(os.path.join(os.path.dirname(__file__))))
    # insert_row()
    # create_table()
    insert_row()
    query()
