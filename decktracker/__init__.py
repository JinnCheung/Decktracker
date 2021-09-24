#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .log import log


log.info("init fuck you")



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

"""