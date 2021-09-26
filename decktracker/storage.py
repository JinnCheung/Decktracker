#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

"""A simple introdution

more description

:Project: https://github.com/JinnCheung/Decktracker
:Author: Jinn Cheung
:Date: 2021/9/27 00:01 
"""

import feather
import pandas as pd
import numpy as np

# import os
# os.chdir(r'C:\Users\111\Desktop')

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
    df.head()

    feather.write_dataframe(df, 'data.feather')