#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Pull stock data to local，and offer some query functions.

more description

:Project: https://github.com/JinnCheung/Decktracker
:Author: Jinn Cheung
:Date: 2021/9/28 13:55 
"""

from decktracker import config, ts_api
from pprint import pp

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
    pp(config.get("tushare").get("api"))
