import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set()
# os.listdir()

dfcrime = pd.read_csv(r"C:\Users\bosko\Documents\ULERPITON3\LatihanPiton\LATIHAN\london_crime_by_lsoa.csv")

# Rename nama kolom
dfcrime.rename(columns={'borough':'city'}, inplace=True)

# Untuk mengecek kolom
dfcrime.info()

# Untuk mengecek statistik numerik
dfcrime.describe()

# Untuk mengecek statistik non numerik
dfcrime.describe(include = "O")

# Untuk apakah ada data NULL
dfcrime.isnull()

# ------------------------------------------------------------------------------------------
# SOAL1, Apa perubahan jumlah kasus dari 2011 ke 2016?
soal1 = dfcrime[
      (dfcrime['year'] >= 2011) &
      (dfcrime['year'] <= 2016)
      ]

soal1sum = soal1.groupby('year', sort=True)['value'].sum()

soal1sum.plot(kind='line')

# Kesimpulan : Tingkat kasus kalau dilihat dari tahun 2011, cenderung menurun sampai dengan tahun 2014, namun setelah itu kembali naik sampai dengan tahun 2016


# -------------------------------------------------------------------------------------------
# SOAL2, Apa tindak kriminal yang paling sering terjadi dan di daerah mana pada tahun 2016?
soal2 = dfcrime[
        (dfcrime['value']>0)&
        (dfcrime['year']==2016)
    ].groupby('city')[['major_category','value']].max()

nilaimaksimum = soal2.value.max()

soal2[(soal2['value']==nilaimaksimum)]

# soal2reset = soal2.reset_index()
# soal2reset[['value']].max()

# soal2.plot.pie(y='value', figsize=(7,7))
soal2.plot.pie(y='value', title="Violence against person by borough", \
                   autopct='%1.1f%%',  \
                   shadow=False)

plt.legend(fontsize=6, loc='upper center', 
           bbox_to_anchor=(0.5, -0.04), ncol=2)    

plt.show()    
# plt.title('Violence Agains the Person on Each City')
# plt.ylabel('Total Event')
# plt.xlabel('City')

# Kesimpulan : Pada tahun 2016, dari semua kota yang ada, kategori yang paling banyak adalah Violence Agains the Person di kota Westminster sejumlah 149 kasus

# ------------------------------------------------------------------------------------------
# SOAL3, Kota manakah yang memiliki jumlah kejahatan terbanyak
# dfcrime.year.unique()

# dfcrime.fillna(0)

soal3 = dfcrime.groupby('city')['value'].sum().reset_index(name='Total')
jmljahatmax = soal3.Total.max()

soal3[(soal3['Total']==jmljahatmax)]
# Kesimpulan : Kota yang memiliki kejahatan terbayak di rentang waktu tersebut adalah Westminster dengan jumlah 455028 kasus


# SOAL4, Kota manakah yang memiliki jumlah kejahatan paling sedikit
soal4 = dfcrime.groupby('city')['value'].sum().reset_index(name='Total')
jmljahatmin = soal4.Total.min()

soal4[(soal4['Total']==jmljahatmin)]

# Kesimpulan : Kota yang memiliki kejahatan paling sedikit di rentang waktu tersebut adalah City of London dengan jumlah kasus 780 kasus, sehingg City of London bisa di simpulkan juga kota paling aman

# -----------------------------------------------------------------------------------------
# SOAL5, Munculkan grafik total kejadian kejahatan masing2 kota pada tahun 2015
soal5 = dfcrime[
        (dfcrime['year']==2015)
    ].groupby('city')['value'].sum().reset_index(name='Total')

soal5.plot(x='city',y='Total',kind='bar',figsize=(9,8))
plt.title('Jumlah Kejahatan Tahun 2015')
plt.ylabel('Kejahatan (kasus)')
plt.xlabel('Kota')
plt.show()
