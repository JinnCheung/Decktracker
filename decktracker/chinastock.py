#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Pull stock data to local，and offer some query functions.

more description

:Project: https://github.com/JinnCheung/Decktracker
:Author: Jinn Cheung
:Date: 2021/9/28 13:55 
"""
import time
import os
from itertools import product
from pyarrow import Table
import pyarrow.parquet as pq
import pandas as pd
from decktracker import config, ts_api
from pprint import pp


def gen_kwlist(params: dict) -> list:
    """generate a list of key-word parameter for an api

    :param params: api preset params
    :return: a list of key-words for send to api
    """
    no_iter_params = dict()
    iter_params = list()

    for k, v in params.items():
        if isinstance(v, list):
            iter_params.append([{k: i} for i in v])
        else:
            if bool(v):
                no_iter_params.update({k: v})

    if len(iter_params) > 0:
        kwlist = list()
        for i in product(*iter_params):
            combine_dict = dict()
            for d in i:
                combine_dict = dict(combine_dict, **d)
            kwlist.append(combine_dict)

        return [dict(kw, **no_iter_params) for kw in kwlist]
    else:
        return [no_iter_params]


def load_stock_basic():
    api_setting = config.get('tushare').get('api').get('stock_basic')
    stock_basic_local = os.path.abspath(os.path.join(config.get('folders').get('data'), 'stock_basic.parquet'))
    params = gen_kwlist(api_setting.get("params"))[0]
    fields = api_setting.get("fields")
    params.update({'fields': ','.join(fields.keys())})

    dataframe = ts_api.query('stock_basic', **params)
    table = Table.from_pandas(df=dataframe)
    pq.write_table(table, stock_basic_local)


def get_local_stock_basic():
    stock_basic_local = os.path.abspath(os.path.join(config.get('folders').get('data'), 'stock_basic.parquet'))
    return pq.read_pandas(stock_basic_local, columns=['ts_code', 'list_date']).to_pandas()


"""
请求一日的数据，获取全部当日全部数据。
请求一票数据，获取单一全部股票数据。
Parquet不支持多次写入，因此写两种方法
1. 初次请求一票数据，将历史数据保存至quotations/symbol.date.parquet的文件中，并在recent.db的stock_basic中记录存档文件位置，存档日期。
2. 第二次请求日数据，将日数据数据保存至 quotations/recent.db数据库中
3. 查询票数据时，先查询parquet是否满足，然后查询recent.sb是否满足。
4. 执行归档操作时，将同时读取parquet表和recent.db，再保存为parquet，更新记录，删除旧文件。
5. 如某日查询无数据，检查日历，返回日历的上一交易日，仍无数据，检查停牌日，仍无数据，报错。
>>> s = chinastock('SZ000001')
>>> s.daily(start_date='20210101',end_date='20210101')
>>> s.close_price(date='20210101',adj=None)

"""

if __name__ == "__main__":
    stock_basic_local = os.path.abspath(os.path.join(config.get('folders').get('data'), 'stock_basic.parquet'))

    t
    table = Table.from_pandas(df=dataframe)
    pq.write_table(table, stock_basic_local)
    # print(get_local_stock_basic())
