#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""A simple introdution

more description

:Project: https://github.com/JinnCheung/Decktracker
:Author: Jinn Cheung
:Date: 2021/9/27 20:02 
"""
import tushare as ts

pro = ts.pro_api("eac2dfd8378cc20be48580065f31e1f4f001998275b79ee15d2b7086")

if __name__ == '__main__':
    df = pro.trade_cal(exchange='', start_date='20180901', end_date='20181001',
                       fields='exchange,cal_date,is_open,pretrade_date', is_open='0')

    print(df)

"""

https://github.com/shidenggui/easyquotation

计划从Baostock中获取基本信息。
再从tushare交叉验证。
建立可信历史数据库。
实时行情与历史行情分开获取。

findatapy- 获取彭博终端，Quandl和雅虎财经的数据

googlefinance- 从谷歌财经获取实时股票价格

yahoo-finance- 从雅虎财经下载股票报价，历史价格，产品信息和财务报表

pandas-datareader- 从多个数据源获取经济/金融时间序列，包括谷歌财经，雅虎财经，圣路易斯联储(FRED)，OECD, Fama/French，世界银行，欧元区统计局等，是Pandas生态系统的重要组成

pandas-finance- 提供高级接口下载和分析金融时间序列

pyhoofinance- 从雅虎财经批量获取股票数据

yfinanceapi- 从雅虎财经获取数据

yql-finance- 从雅虎财经获取数据

ystockquote- 从雅虎财经获取实时报价

wallstreet- 实时股票和期权报价

stock_extractor- 从网络上爬取股票信息

Stockex- 从雅虎财经获取数据

finsymbols- 获取全美证券交易所，纽约证券交易所和纳斯达克上市公司的详细数据

inquisitor- 从Econdb获取经济数据，Econdb是全球经济指标聚合器

chinesestockapi- 获取A股数据

exchange- 获取最新的汇率报价

ticks- 命令行程序，获取股票报价

pybbg- 彭博终端COM的Python接口

ccy- 获取外汇数据

tushare- 获取中国股票，基金，债券和期货市场的历史数据

jsm- 获取日本股票市场的历史数据

cn_stock_src- 从不同数据源获取中国的股票数据

coinmarketcap- 从coinmarketcap获取数字货币数据

after-hours- 获取美股盘前和盘后的市场价格

bronto-python- 整合Bronto API接口

pytdx- 获取中国国内股票的实时报价

pdblp- 整合Pandas和彭博终端的公共接口

tiingo- 从Tiingo平台获取股票日K线和实时报价/新闻流

IEX- 从IEX交易所获取股票的实时报价和历史数据

alpaca-trade-api- 从Alpaca平台获取股票实时报价和历史数据，并提供交易接口交易美股

metatrader5- 集成Python和MQL5交易平台，适合外汇交易

akshare- 获取中国股票，基金，债券和宏观经济数据

yahooquery- 从雅虎财经获取数据

investpy- 从英为财经(Investing.com)获取数据

yliveticker- 从雅虎财经通过Websocket获取实时报价
"""