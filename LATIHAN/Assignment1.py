# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 20:25:40 2022

@author: bosko
"""

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

dfcrime = pd.read_csv("london_crime_by_lsoa.csv")

# Untuk mengecek kolom
dfcrime.info()

# Untuk mengecek statistik numerik
dfcrime.describe()

# Untuk mengecek statistik non numerik
dfcrime.describe(include = "O")

# Select single column (called series)
databaru = dfcrime['lsoa_code']
databaru

# Select multiple column (called dataframe)
databaru = dfcrime[['lsoa_code','borough']]
databaru

dfcrime['month'].plot.hist()

soal1 = dfcrime[['year','value']]
soal1

soal1_1 = soal1[
      (soal1['year'] >= 2011) &
      (soal1['year'] <= 2016)
      ]

soal1_1.groupby('year', sort=True)['value'].sum()