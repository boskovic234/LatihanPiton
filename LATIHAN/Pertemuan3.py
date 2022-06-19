import numpy as np
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/ardhiraka/PFDS_sources/master/nbaallelo.csv')

nba = df.copy()

# print (df)
# A = len(df)
# B = df.shape
# C = df.head(5)
# D = df.tail(2)
# E = df.info()
# pd.set_option("display.max.columns", None)
# pd.set_option("display.precision", 2)

# df.info() #untuk melihat summary strutkur data table
# desc = df.describe() #statistika deskriptif (informasi mean, median, modus, dll)

# print (desc)

# print(df.loc[10:15])

# print(df["team_id"].value_counts())
# print(df["fran_id"].value_counts())
# print(df.loc[df["fran_id"] == "Lakers", "team_id"].value_counts())

# revenues = pd.Series([1000, 2000, 3000, 4000])
# print(revenues.values)


# print(df)

# current_decaded = df[df["year_id"] > 2010]
# print(current_decaded)


nba[nba["fran_id"] == "Knicks"].groupby("year_id")["pts"].sum().plot()

# <matplotlib.axes._subplots.AxesSubplot at 0x129e72790>