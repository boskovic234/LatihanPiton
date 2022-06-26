import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


df_can = pd.read_excel('https://github.com/ardhiraka/PFDS_sources/blob/master/Canada.xlsx?raw=true',
                       sheet_name='Canada by Citizenship',
                       skiprows=range(20),
                       skipfooter=2)

print ('Data read into a pandas dataframe!')

# Rubah Style Grafik
print("Model grafik tersedia")
print(plt.style.available) # untuk menampilkan style apa saja
mpl.style.use(['ggplot']) # optional: for ggplot-like style

# # Munculin info dari file tersebut dan tipe data nya
# df_can.info() 

# # Untuk memunculkan informasi ada kolom apa saja
# print(df_can.columns.values)

# # Untuk melihat shape/ukuran data, berapa [baris, kolom]
# print(df_can.shape)

# # Untuk rename kolom
df_can.rename(columns={'OdName':'Country', 'AreaName':'Continent', 'RegName':'Region'}, inplace=True)
# print(df_can.columns)

# # Untuk cek apakah di masing2 kolom ada values NULL
# print(df_can.isnull().sum())

# # Untuk select / menampilkan kolom yang dibutuhkan saja
# print(df_can.Country)
# print(df_can[["Country","Continent"]])

df_can.set_index('Country', inplace=True)
df_can.index.name = None

# # Untuk query menampilkan value data tertentu (haru)
# print(df_can.loc['Japan'])

# print(df_can.iloc[87])
# print(df_can[df_can.index == 'Japan'].T.squeeze())

# print(df_can.loc['Japan', 2013])

df_can.columns = list(map(str, df_can.columns))

# # Untuk bikin parameter value sort
years = list(map(str, range(1980, 2014)))
# print(years)

# # Single Filtering
# condition = df_can['Continent'] == 'Asia'
# # print (condition)
# print(df_can[condition])

# # Multiple Filtering
# condition2 = df_can[(df_can['Continent']=='Asia') & (df_can['Region']=='Southern Asia')]
# # print(condition2)
# print(df_can[condition2])

# Load data to show in graph
# haiti = df_can.loc['Haiti', 2015] # passing in years 1980 - 2013 to exclude the 'total' column
# japan = df_can.loc['Japan', [2013,2014,2015]]
# japan = df_can.loc['Japan', [1980, 1981, 1982, 1983, 1984, 1985]]
japan = df_can.loc['Japan', years]
japan.index = japan.index.map(int)
print(japan)
japan.plot(kind='line')

plt.title('Immigration from Japan')
plt.ylabel('Number of immigrants')
plt.xlabel('Years')

plt.text(2000, 1000, 'Disini') # see note below


plt.show()