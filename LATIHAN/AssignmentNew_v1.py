import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.colors as mcolors


nama = input('Masukkan nama anda :')
print('Selamat datang di pusat informasi kejahatan di Inggeris,',nama.title())

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

dfcrime.head(10)


# SOAL1, Kota manakah yang memiliki kasus kejahatan paling banyak
S1 = dfcrime.groupby('city')['value'].sum().reset_index(name='Total')
jmljahatmax = S1.Total.max()

S1[(S1['Total']==jmljahatmax)]

# ---------------------------------------------------------------------------------------------------------------------------
# SOAL2, berdasarkan temuan di SOAL1, tampilkan komposisi header kategori kejahatannya

S2 = dfcrime[dfcrime['city']=='Westminster']
S2_1 = S2.groupby('major_category')['value'].sum()

colors = ['#ff0000','#0000ff','#660066','#b3b300','#ff00ff','#ffff00','#ff9999','#009933','#003311','#33ff77','#ff884d','#cc4400','#802b00','#000000']

S2_1.groupby(['major_category']).sum().plot(kind='pie', figsize=(14, 6),
                            startangle=90,    
                            autopct='%1.1f%%', 
                            labels=None,       
                            shadow=False,       
                            pctdistance=1.12,
                            colors=colors)

plt.title('Komposisi kejahatan di kota Westminster', y=1.10) 
plt.axis('equal') 
plt.legend(labels=S2_1.index, 
           loc='upper right')
plt.show()

# ----------------------------------------------------------------------------------------------------------------------------------------
# SOAL3, berdasarkan SOAL2, kategori paling banyak adalah Theft and Handling, tampilkan jenis2 detail kejahatannya.
S3 = S2[S2['major_category']=='Theft and Handling']
S3_1 = S3.groupby(['minor_category'])['value'].sum()

S3_1.plot(x='minor_category',y='value',kind='bar',figsize=(8,6))
plt.title('Jumlah Kejahatan Kota Wesminster')
plt.ylabel('Kejahatan (kasus)')
plt.xlabel('Jenis Kejahatan')
plt.show()

# ----------------------------------------------------------------------------------------------------------------------------------------
# SOAL4, Kota manakah yang memiliki jumlah kejahatan paling sedikit
S4 = dfcrime.groupby('city')['value'].sum().reset_index(name='Total')
jmljahatmin = S4.Total.min()
S4[(S4['Total']==jmljahatmin)]

# ------------------------------------------------------------------------------------------
# SOAL5, Bagaimana trend kejahatan setiap tahun nya
S5 = dfcrime.groupby('year', sort=True)['value'].sum()

S5.plot(kind='line',figsize=(16,8))
plt.title('Trend Kejahatan')
plt.ylabel('Kejahatan (kasus)')
plt.xlabel('Tahun')
plt.show()

# Summary, 
# 1. Dari data2 diatas, bisa disimpulkan bahwa kota yang memiliki jumlah kejahatan terbanyak adalah Westminster dengan jumlah 455028 kasus.
# 2. Dengan kategori kejahatan terbesar Theft Handling, sebesar 61% dibanding kategori kejahatan lainnya
# 3. Di dalam kategori Theft Handling, yang paling banyak adalah Other Theft, Other Theft Person, Theft from Shops sebagai Top 3 kasus
# 4. Kota yang paling sedikit kasus kejahatan adalah City of London, bisa di asumsikan ini adalah kota teraman
# 5. Sejak tahun 2008 kasus kejahatan menurun, namun setiap 2 tahun mengalami kenaikan dan penurunan secara fluktuatif