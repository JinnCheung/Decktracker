#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""Another portfolio tracking and analysis tool

Modules:
    1. __init__.py : Check the configure.
    #. __main__.py : Command line interactive operations.
    #. log.py : Print colored log on commandline/debug.log.
    #. stock.py : Pull stock data to local HDF file，and offer some query functions.
    #. fund.py : Pull fund data to local HDF file，and offer some query functions.
    #. delivery.py : Pull fund data to local HDF file，and offer some query functions.
    #. tracker.py : when we sell.
    #. prisma.py : which to buy.

:Project: https://github.com/JinnCheung/Decktracker
:Author: Jinn Cheung
:Date: 2021/9/25 08:04
"""
import os
import argparse
from requests.exceptions import ConnectionError
import toml
import tushare


def load_toml_config(folder: str) -> dict:
    """load configure of Decktracker

    Specify the configuration file in the command line argument, or load it in the default folder.

    :param folder: a folder of config.toml.
    :return: a dict of configure.
    """
    parser = argparse.ArgumentParser(description='Portfolio tracking and analysis tools')

    parser.add_argument('-c', '--config', metavar='config.toml', dest='config_file', action='store',
                        help='a configuration file in TOML format.')

    args = parser.parse_args()

    config_file = os.path.abspath(os.path.join(folder, 'config.toml')) if args.config_file is None else args.config_file

    if os.path.exists(config_file):
        return toml.load(config_file)
    else:
        raise FileNotFoundError("%s not found. There is an sample of config.toml in /docs." % config_file)


project_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

config = load_toml_config(project_folder)

folders = config.get('folders')

if folders.get('root_folder') == '':
    folders.update({'root_folder': project_folder})

folders.update({'data_folder': os.path.abspath(os.path.join(folders.get('root_folder'), folders.get('data_folder')))})

# try:
#     pro = tushare.pro_api(config.get('tushare').get('token'))
#     pro.trade_cal(exchange='', start_date='20210101', end_date='20210101')
#     # pro.hk_daily(ts_code='00001.HK', start_date='20210101', end_date='20210901')
#     print("Tushare Connected.")
# except ConnectionError as e:
#     print("Tushare Connect Fail.")
# except Exception as e:
#     print("Tushare Connect Fail: %s" % e.args[0])
#
# if __name__ == '__main__':
#     df = pro.query('trade_cal')
#     print(df)

"""
1. 数据准备（__init__.py）
  1.1 测试接口畅通（雪球接口、tushare接口、akshare接口、redis缓存）
  1.2 更新股票清单、基金清单、交易日历。
  1.3 准备flask操作界面。
2. 从main获取配置文件（__main__.py）
  2.1 检查配置文件
  2.2 检查数据情况（data/delivery.db  data/quotation.db）
3. 必要工具模块：
  3.1 log.py 定制日志功能。
  3.2 storage.py 定制数据帧储存。
  3.3 cache.py 定制函数缓存。
  3.4 cli.py 命令行操作界面。
  3.5 app.py 浏览器操作界面。
  3.5 stock.py 股票实时和历史行情数据、财务数据拉取到本地，并提供查询接口。（使用feather或Hdf5保存到本地）
  3.6 fund.py 基金实时和历史行情数据拉取到本地，提供查询接口（使用feather或Hdf5保存到本地）。
  3.7 delivery.py 个人交易记录录入、导入和删改（使用sqllite3保存到本地）
  3.8 tracker.py 持仓分析器


准备操作，登记依赖，生成requirement.txt。
pipreqs . --force 

安装feather格式支持
pip install feather-format
"""
