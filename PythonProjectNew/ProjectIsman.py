#%%
from sre_parse import CATEGORIES
from turtle import clear
import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.colors as mcolors
import math
import statistics
from wordcloud import WordCloud, STOPWORDS
import os


dfpol = pd.read_csv(r'C:\Users\bosko\Documents\ULERPITON3\LatihanPiton\PythonProjectNew\police_deaths_in_america.csv')

# WORKING AREA (REMARK SEBELUM DI COMPILE)

# untuk compile 
# python -m py_compile namafile.py

# # Untuk mengecek kolom
# dfpol.info()

# # Untuk mengecek statistik numerik
# dfpol.describe()

# # Untuk mengecek statistik non numerik
# dfpol.describe(include = "O")

# # Untuk apakah ada data NULL
# dfpol.isnull()

# dfpol.head(10)

# # Bagaimana Trend Kejadian Kematian pada data tersebut
# # old code
# trend = dfpol.groupby('Year')['Name'].count()
# plt.locator_params('x', nbins=18)
# plt.locator_params('y', nbins=12)
# trend.plot(kind='line',figsize=(15,6))
# plt.title('Police died in America')
# plt.ylabel('Died (Case)')
# plt.xlabel('Year')
# plt.text(2023, 630, 'Highest Case')

# --------------------------------------------
# trend = dfpol[(dfpol['Rank']!='K9')]
# trendc = trend.groupby('Year')['Name'].count()
# plt.locator_params('x', nbins=18)
# plt.locator_params('y', nbins=12)
# trendc.plot(kind='line',figsize=(15,6))
# plt.title('Police died in America')
# plt.ylabel('Died (Case)')
# plt.xlabel('Year')

# # Rata2 Kasus per tahun
# rata2kasus = round(statistics.mean(trendc))
# plt.text(2023, 630, 'Highest Case')
# plt.text(1800, 500, 'Rata-rata : '+ str(rata2kasus)+' kasus')


# # Tahun berapa kasus kematian polisi paling banyak terjadi
# # dfpol[(dfpol['Year']==1930)]
# S2 = trendc.reset_index('Year')
# S2total = S2.Name.max()
# npmaxtahun = np.array(S2[(S2['Name']==S2total)])
# maxtahun = npmaxtahun[0,0]


# # Rata2 kasus per bulan by tahun
# trendmonth = dfpol[(dfpol['Year']==2020) & (dfpol['Rank']!='K9')]
# trendmonthc = trendmonth.groupby('Month',sort=False)['Name'].count()
# round(statistics.mean(trendmonthc))
# plt.locator_params('x', nbins=18)
# plt.locator_params('y', nbins=12)
# trendmonthc.plot(kind='line',figsize=(15,6))
# plt.title('Police died in America')
# plt.ylabel('Died (Case)')
# plt.xlabel('Month')

# # Kasus paling banyak di tahun tersebut
# maxcase = trendmonth.groupby('Cause_of_Death')['Name'].count()
# maxcasemax = maxcase.max()
# maxcasereset = maxcase.reset_index('Cause_of_Death')
# npmaxcase = np.array(maxcasereset[(maxcasereset['Name']==maxcasemax)])
# maxcase = npmaxcase[0,0]
# print(maxcase)

# # Rank paling banyak di tahun tersebut
# maxrank = trendmonth.groupby('Rank')['Name'].count()
# maxrankmax = maxrank.max()
# maxrankreset = maxrank.reset_index('Rank')
# npmaxrank = np.array(maxrankreset[(maxrankreset['Name']==maxrankmax)])
# maxrank = npmaxrank[0,0]
# print(maxrank)

# # State paling banyak di tahun tersebut
# maxstate = trendmonth.groupby('State')['Name'].count()
# maxstatemax = maxstate.max()
# maxstatemaxreset = maxstate.reset_index('State')
# maxstatemaxreset[(maxstatemaxreset['Name']==maxstatemax)]
# npmaxstate = np.array(maxstatemaxreset[(maxstatemaxreset['Name']==maxstatemax)])
# state = npmaxstate[0,0]
# print(state)

# # Departemen paling banyak di tahun tersebut
# maxdept = trendmonth.groupby('Department')['Name'].count()
# maxdeptmax = maxdept.max()
# maxdeptreset = maxdept.reset_index('Department')
# npmaxdept = np.array(maxdeptreset[(maxdeptreset['Name']==maxdeptmax)])
# deptname = npmaxdept[0,0]
# print(deptname)


# print(dfpol['Year'].unique())


# # Penyebab Kematian
# trendpie = trend.groupby('Cause_of_Death')['Name'].count()
# trendpie.plot(kind='barh', figsize=(15, 12), color='red')
# plt.ylabel('Penyebab Kematian')
# plt.xlabel('Tahun')
# plt.title('Penyebab Kematian Polisi Amerika Serikat [1791 - 2022]')
# plt.show()

# # Visualisasi Wordcloud
# cod = dfpol.Cause_of_Death.unique()
# codnp = np.array_str(cod)
# stopwords = set(STOPWORDS)

# codwd = WordCloud(background_color='white',
#     max_words=2000,
#     stopwords=stopwords)

# codwd.generate(codnp)
# plt.imshow(codwd, interpolation='bilinear')
# plt.axis('off')
# plt.show()


# # # COVID19
# c19year = int(input('Masukkan tahun [2020 - 2022] : '))
# c19 = dfpol[(dfpol['Rank']!='K9') & (dfpol['Cause_of_Death']=='COVID19') & (dfpol['Year']==c19year)]
# trendc19 = c19.groupby('Month')['Name'].count().reset_index()
# trendc19.rename(columns={'Name':'Kasus Covid'}, inplace=True)

# # UNTUK CARI BULAN TERBANYAK KASUS DI TAHUN TERSEBUT
# maxmc19 = trendc19['Kasus Covid'].max()
# npmaxmc19 = np.array(trendc19[(trendc19['Kasus Covid']==maxmc19)])
# maxmonthmc19 = str(npmaxmc19[0,0])

# # UNTUK CARI KOTA TERBANYAK KASUS DI TAHUN TERSEBUT
# cityc19 = c19.groupby('State')['Name'].count().reset_index()
# maxcityc19 = cityc19['Name'].max()
# npmaxcityc19 = np.array(cityc19[(cityc19['Name']==maxcityc19)])
# maxstatec19 = str(npmaxcityc19[0,0])

# sort_order = ['January','February','March',
#                 'April','May','June',
#                 'July','August','September',
#                 'October','November','December']

# trendc19.index = pd.CategoricalIndex(trendc19['Month'],categories=sort_order,ordered=True)
# trendc19 = trendc19.sort_index().reset_index(drop=True)

# # plt.locator_params('x', nbins=18)
# # plt.locator_params('y', nbins=12)
# trendc19.plot(x='Month',y='Kasus Covid',kind='bar',figsize=(15,6),color='red')
# # trendc19.plot(x='Month',y='Kasus Covid',kind='line',figsize=(15,6),color='blue',marker='*')
# trendmonthmeanc19 = round(statistics.mean(trendc19['Kasus Covid']))

# plt.ylabel('Kematian (Kasus)')
# plt.xlabel('Bulan')
# plt.title('Trend kasus COVID di Amerika tahun '+str(c19year)+' (Rata-rata : '+str(trendmonthmeanc19)+' kasus)')

# print('Pada tahun '+str(c19year)+', kasus COVID19 paling banyak terjadi di bulan '+maxmonthmc19+', dengan kota '+maxstatec19+
# ' menduduki peringkat terbanyak polisi terinfeksi COVID19 di tahun ini.')

# plt.show()

#%%

# #ADJUST TOTAL
# trend = dfpol[(dfpol['Rank']!='K9')]
# trendc = trend.groupby('Year')['Name'].count()
# matplotlib.pyplot.rcdefaults()
# plt.locator_params('x', nbins=18)
# plt.locator_params('y', nbins=12)
# trendc.plot(kind='line',figsize=(15,6),color='red')

# plt.ylabel('Kematian (Kasus)')
# plt.xlabel('Tahun')

# # Cari tahun dengan kasus terbanyak
# S2 = trendc.reset_index('Year')
# S2total = S2.Name.max()
# npmaxtahun = np.array(S2[(S2['Name']==S2total)])
# maxtahun = str(npmaxtahun[0,0])
# maxtahuncase = str(npmaxtahun[0,1])


# # Rata2 Kasus per tahun
# rata2kasus = round(statistics.mean(trendc))
# plt.text(1973, 610, 'Kasus Tertinggi: '+maxtahun+' ('+maxtahuncase+')'+' ->')
# plt.text(1800, 500, 'Rata-rata : '+ str(rata2kasus)+' kasus')
# plt.title('Trend kematian polisi Amerika tahun 1791 - 2022')

# plt.annotate('',                      
#         xy=(2017, 500),             
#         xytext=(2013, 280),         
#         xycoords='data',         
#         arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='blue', lw=2)
#     )

# plt.annotate('2019 - PANDEMI COVID19', 
#         xy=(2008, 270),                    
#         rotation=82.5,                  
#         va='bottom',                    
#         ha='left',                      
#     )

# plt.show()

# trendcsns = pd.DataFrame(trendc)
# trendcsns.index = map(float,trendcsns.index)
# trendcsns.reset_index(inplace=True)
# trendcsns.columns = ['Tahun','Total Kasus']
# plt.figure(figsize=(15,6))
# sns.set(font_scale=1.0)
# sns.set_style('whitegrid')
# ax = sns.regplot(x='Tahun', y='Total Kasus', data=trendcsns,color='green',marker='+')

# plt.title('Reggression View')

# plt.show()



# START PRORGAM
print('👮‍♂️ ⚠️  👮‍♀️')
namaanda = input("Masukkan nama anda : ")

# control = {1:'ya',2:'tidak'}

while True:
    
    os.system('cls')
    print('👮‍♂️ ⚠️  👮‍♀️')
    print(" ")
    print("Selamat datang di pusat informasi Kepolisian Amerika Serikat, "+namaanda.title())
    print(" ")
    print("Informasi apa yang anda butuhkan, silahkan pilih salah satu :")
    print("1. Data trend jumlah kematian polisi di Amerika Serikat")
    print("2. Data informasi kematian polisi per tahun")
    print("3. Visualiasi grafik Penyebab Kematian Polisi Amerika Serikat [1791 - 2022]")
    print("4. Visualiasi WordCloud Penyebab Kematian Polisi Amerika Serikat [1791 - 2022]")
    print("5. Data trend kasus COVID di Amerika")
    print(" ")
    pilihan = input("Pilihan anda no : ")
    
    if pilihan.lower() == "1":
        trend = dfpol[(dfpol['Rank']!='K9')]
        trendc = trend.groupby('Year')['Name'].count()
        matplotlib.pyplot.rcdefaults()
        plt.locator_params('x', nbins=18)
        plt.locator_params('y', nbins=12)
        trendc.plot(kind='line',figsize=(15,6),color='red')

        plt.ylabel('Kematian (Kasus)')
        plt.xlabel('Tahun')

        # Cari tahun dengan kasus terbanyak
        S2 = trendc.reset_index('Year')
        S2total = S2.Name.max()
        npmaxtahun = np.array(S2[(S2['Name']==S2total)])
        maxtahun = str(npmaxtahun[0,0])
        maxtahuncase = str(npmaxtahun[0,1])


        # Rata2 Kasus per tahun
        rata2kasus = round(statistics.mean(trendc))
        plt.text(1973, 610, 'Kasus Tertinggi: '+maxtahun+' ('+maxtahuncase+')'+' ->')
        plt.text(1800, 500, 'Rata-rata : '+ str(rata2kasus)+' kasus')
        plt.title('Trend kematian polisi Amerika tahun 1791 - 2022')

        plt.annotate('',                      
                xy=(2017, 500),             
                xytext=(2013, 280),         
                xycoords='data',         
                arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='blue', lw=2)
            )

        plt.annotate('2019 - PANDEMI COVID19', 
                xy=(2008, 270),                    
                rotation=82.5,                  
                va='bottom',                    
                ha='left',                      
            )

        plt.show()

        trendcsns = pd.DataFrame(trendc)
        trendcsns.index = map(float,trendcsns.index)
        trendcsns.reset_index(inplace=True)
        trendcsns.columns = ['Tahun','Total Kasus']
        plt.figure(figsize=(15,6))
        sns.set(font_scale=1.0)
        sns.set_style('whitegrid')
        ax = sns.regplot(x='Tahun', y='Total Kasus', data=trendcsns,color='green',marker='+')

        plt.title('Reggression View')

        plt.show()
        
        print('')
        ulang = input("Apakah anda ingin kembali ke menu utama ? (Ya/Tidak) : ")
        if ulang.lower() == "tidak":
            break
        

    if pilihan.lower() == "2":
        tahun = int(input('Masukkan Tahun Yang Diinginkan [1791 - 2022]: '))
        
        # Informasi Total Kasus
        trend = dfpol[(dfpol['Rank']!='K9')]
        bytahun = trend.groupby('Year')['Name'].count().reset_index()
        bytahun.rename(columns={'Name':'Total_Case'}, inplace=True)
        nptahun = np.array(bytahun[(bytahun['Year']==tahun)])
        countahun = str(nptahun[0,1])
            
        
        # Rata2 kasus per bulan by tahun
        trendmonth = dfpol[(dfpol['Year']==tahun) & (dfpol['Rank']!='K9')]
        trendmonthc = trendmonth.groupby('Month',sort=False)['Name'].count()
        trendmonthmean = round(statistics.mean(trendmonthc))
        print('')
        print('--------------------------------------------')
        print('Total kasus kematian polisi pada tahun',tahun,'adalah sebanyak '+countahun+
              ' kasus, dengan nilai rata-rata kejadian per bulan pada tahun '+str(tahun)+
              ' adalah '+str(trendmonthmean)+' kasus.')
        plt.locator_params('x', nbins=18)
        plt.locator_params('y', nbins=12)
        trendmonthc.plot(kind='bar',figsize=(15,6),color='red')
        
        plt.ylabel('Kematian (Kasus)')
        plt.xlabel('Bulan')
        
        
        # Kasus paling banyak di tahun tersebut
        maxcase = trendmonth.groupby('Cause_of_Death')['Name'].count()
        maxcasemax = maxcase.max()
        maxcasereset = maxcase.reset_index('Cause_of_Death')
        npmaxcase = np.array(maxcasereset[(maxcasereset['Name']==maxcasemax)])
        maxcase = str(npmaxcase[0,0])
        # print('')
        # print('--------------------------------------------')
        # print('Kematian paling banyak dari case'+maxcase+'.')
        
        # Rank paling banyak di tahun tersebut
        maxrank = trendmonth.groupby('Rank')['Name'].count()
        maxrankmax = maxrank.max()
        maxrankreset = maxrank.reset_index('Rank')
        npmaxrank = np.array(maxrankreset[(maxrankreset['Name']==maxrankmax)])
        maxrank = str(npmaxrank[0,0])
        # print('')
        # print('--------------------------------------------')
        # print('Kematian paling banyak dari rank'+maxrank+'.')
        
        # State paling banyak di tahun tersebut
        maxstate = trendmonth.groupby('State')['Name'].count()
        maxstatemax = maxstate.max()
        maxstatemaxreset = maxstate.reset_index('State')
        maxstatemaxreset[(maxstatemaxreset['Name']==maxstatemax)]
        npmaxstate = np.array(maxstatemaxreset[(maxstatemaxreset['Name']==maxstatemax)])
        state = str(npmaxstate[0,0])
        # print('')
        # print('--------------------------------------------')
        # print('Kematian paling banyak dari state'+state+'.')
        
        # Departemen paling banyak di tahun tersebut
        maxdept = trendmonth.groupby('Department')['Name'].count()
        maxdeptmax = maxdept.max()
        maxdeptreset = maxdept.reset_index('Department')
        npmaxdept = np.array(maxdeptreset[(maxdeptreset['Name']==maxdeptmax)])
        deptname = str(npmaxdept[0,0])
        # print('')
        # print('--------------------------------------------')
        # print('Kematian paling banyak dari departement '+deptname+'.')
        
        
        print('')
        print('Kematian polisi pada tahun '+str(tahun)+' di dominasi oleh kasus '+maxcase+
              ', pangkat yang paling banyak mengalami kematian pada tahun ini adalah '+maxrank+', selain itu kota '+state+
              ' menyumbang kasus terbanyak pada tahun ini, dan juga yang berasal dari department '+deptname+'.')
        
        plt.title('Kematian polisi di America pada tahun '+str(tahun))
        plt.show()
        print('')

        ulang = input("Apakah anda ingin kembali ke menu utama ? (Ya/Tidak) : ")
        if ulang.lower() == "tidak":
            break

    if pilihan.lower() == "3":
        
        trend = dfpol[(dfpol['Rank']!='K9')]
        trendpie = trend.groupby('Cause_of_Death')['Name'].count()
        trendpie.plot(kind='barh', figsize=(15, 12), color='red')
        plt.ylabel('Penyebab Kematian')
        plt.xlabel('Total Kasus')
        plt.title('Penyebab Kematian Polisi Amerika Serikat [1791 - 2022]')
        plt.show()
        
        print('')
        ulang = input("Apakah anda ingin kembali ke menu utama ? (Ya/Tidak) : ")
        if ulang.lower() == "tidak":
            break
    
    if pilihan.lower() == "4":
        
        cod = dfpol.Cause_of_Death.unique()
        codnp = np.array_str(cod)
        stopwords = set(STOPWORDS)

        codwd = WordCloud(background_color='white',
            max_words=2000,
            stopwords=stopwords)

        codwd.generate(codnp)
        plt.imshow(codwd, interpolation='bilinear')
        plt.axis('off')
        plt.show()
        
        print('')
        ulang = input("Apakah anda ingin kembali ke menu utama ? (Ya/Tidak) : ")
        if ulang.lower() == "tidak":
            break

    if pilihan.lower() == "5":
        # matplotlib.pyplot.rcdefaults()
        # COVID19
        c19year = int(input('Masukkan tahun [2020 - 2022] : '))
        c19 = dfpol[(dfpol['Rank']!='K9') & (dfpol['Cause_of_Death']=='COVID19') & (dfpol['Year']==c19year)]
        trendc19 = c19.groupby('Month')['Name'].count().reset_index()
        trendc19.rename(columns={'Name':'Kasus Covid'}, inplace=True)

        # UNTUK CARI BULAN TERBANYAK KASUS DI TAHUN TERSEBUT
        maxmc19 = trendc19['Kasus Covid'].max()
        npmaxmc19 = np.array(trendc19[(trendc19['Kasus Covid']==maxmc19)])
        maxmonthmc19 = str(npmaxmc19[0,0])
        maxmonthmc19val = str(npmaxmc19[0,1])

        # UNTUK CARI KOTA TERBANYAK KASUS DI TAHUN TERSEBUT
        cityc19 = c19.groupby('State')['Name'].count().reset_index()
        maxcityc19 = cityc19['Name'].max()
        npmaxcityc19 = np.array(cityc19[(cityc19['Name']==maxcityc19)])
        maxstatec19 = str(npmaxcityc19[0,0])

        sort_order = ['January','February','March',
                        'April','May','June',
                        'July','August','September',
                        'October','November','December']

        trendc19.index = pd.CategoricalIndex(trendc19['Month'],categories=sort_order,ordered=True)
        trendc19 = trendc19.sort_index().reset_index(drop=True)

        # plt.locator_params('x', nbins=18)
        # plt.locator_params('y', nbins=12)
        trendc19.plot(x='Month',y='Kasus Covid',kind='bar',figsize=(15,6),color='red')
        # trendc19.plot(x='Month',y='Kasus Covid',kind='line',figsize=(15,6),color='blue',marker='*')
        trendmonthmeanc19 = round(statistics.mean(trendc19['Kasus Covid']))

        plt.ylabel('Kematian (Kasus)')
        plt.xlabel('Bulan')
        plt.title('Trend kasus COVID di Amerika tahun '+str(c19year)+' (Rata-rata : '+str(trendmonthmeanc19)+' kasus)')

        print('Pada tahun '+str(c19year)+', kasus COVID19 paling banyak terjadi di bulan '+maxmonthmc19+' sebanyak '+maxmonthmc19val+' kasus, dengan kota '+maxstatec19+
        ' menduduki peringkat terbanyak polisi terinfeksi COVID19 di tahun ini.')

        plt.show()
        
        print('')
        ulang = input("Apakah anda ingin kembali ke menu utama ? (Ya/Tidak) : ")
        if ulang.lower() == "tidak":
            break
        
            # ulang = input("Apakah anda ingin kembali ke menu utama ? (Ya/Tidak) : ")
            # if ulang.lower() == "tidak":
            #     break

#%%