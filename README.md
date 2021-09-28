# Decktracker
another portfolio tracking and analysis tool

## 目标

1. 组合现状分析
2. 历史收益测算
3. 减仓讯号与选股建议

## 功能

1. 交易记录导入
2. 任何时间段持仓切片
3. 组合净值曲线生成
4. 持仓分析
5. 自动运行生成讯号

## 原料

1. 股票和指数日线数据
2. 个人交易记录

## 其他

一次Python规范编程实践。
1. 遵循Python编程哲学。
2. 成为规范共享的第三方模块。
3. 编写完善的文档和单元测试。

主要参考书籍：
1. The Hacker's Guide to Python

## 指定格式

- 日期格式，"%Y%m%d"
- 股票格式，"SZ000001"
- 数据文件格式，"CONTENT.20201231.parquet"

## 使用

1. 从命令行中输入
   - `python -m decktracker --show[-s] all` 列出所有组合名称和简介。
   - `python -m decktracker --show[-s] portfolio_name` 列出 portfolio_name 组合的持仓情况。

2. 从其他程序用引用decktracker的数据
    ```python
    import decktracker as dtk
    

    ```
