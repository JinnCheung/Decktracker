#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""A simple introdution

more description

:Project: https://github.com/JinnCheung/Decktracker
:Author: Jinn Cheung
:Date: 2021/9/27 00:01 
"""

from pyarrow import feather
import pyarrow as pa
from pyarrow import Table
import pyarrow.parquet as pq
import pandas as pd
import numpy as np

if __name__ == '__main__':
    np.random.seed = 2021
    df_size = 10000000

    df = pd.DataFrame({
        'a': np.random.rand(df_size),
        'b': np.random.rand(df_size),
        'c': np.random.rand(df_size),
        'd': np.random.rand(df_size),
        'e': np.random.rand(df_size)
    })
    print(df.head(10))
    t = Table()
    table = t.from_pandas(type_cls=type_cls, df=df)
    pq.write_table(table, 'data.parquet')
    df2 = pq.read_pandas('data.parquet', columns=['a']).to_pandas()
    print(df2.head(10))
    # # feather.write_dataframe(df, 'data.feather')
    # # df2 = feather.read_dataframe('data.feather')
    #
    # print(df2.sample(100))
