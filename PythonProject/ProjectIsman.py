import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tabulate import tabulate

# Untuk load data dari CSV
police = pd.read_csv("police_deaths_in_america.csv")

# Untuk manipulasi tampilan
pd.set_option("display.max.rows", None)
pd.set_option("display.max.column", None)
# pd.set_option("display.precision", 2)

# Untuk cek data berhasil di load
# print(nycdata.head(10))

# untuk compile 
# python -m py_compile namafile.py

print(police.info())
# print(nycdata)

# tahun = input("Masukkan tahun : ")





# meandata = police[
#         ['Rank',
#         'Year',
#         'State']
#         ]

# # print(meandata)
# print("-------------------------------")
# # print(meandata["Rank"].value_counts())
# print("-------------------------------")
# patrolmandata = meandata.loc[
#         (meandata["Rank"] == "Patrolman") &
#          (meandata["State"] == "New York") &
#          (meandata["Year"] > int(tahun))].value_counts(["Rank","State","Year"]).reset_index(name="Count")
# print("-------------------------------")
# print(patrolmandata)         
# df.loc[df["fran_id"] == "Lakers", "team_id"].value_counts()

# print(meandata.describe())

# datarumah = nycdata.loc[(nycdata[""])]


# print(tabulate(nycdata, headers='keys', tablefmt='psql'))


# Munculin Grafik
# data = {'Data1':[1,2,3,4,5],'Data2':[1000,2000,3000,4000,5000]}

# df = pd.DataFrame(data,columns=['Data1','Data2'])
# print(df)

# patrolmandata.plot(x ='Year', y='Count', kind='scatter')
# plt.show()

## -------------------------------BATAS-----------------------
def mean():
    print("Memanggil Function Mean")

    data = {'Data1':[1,2,3,4,5],'Data2':[1000,2000,3000,4000,5000]}

    df = pd.DataFrame(data,columns=['Data1','Data2'])
    print(df)

    df.plot(x ='Data1', y='Data2', kind='scatter')
    plt.show()

def median():
    print("Memanggil Function Median")    

def modus():
    print("Memanggil Function Modus")

def range():
    print("Memanggil Function Range")

def variance():
    print("Memanggil Function Variance")    

def std():
    print("Memanggil Function Standard Deviation")

def prob():
    print("Memanggil Function Probability Distribution")       

def deadyear():
        matitahun = police[["Year"]].value_counts(["Year"]).reset_index(name='Count')
        
        # matitahundf = pd.DataFrame(matitahun, columns=["Years"])
        print(matitahun)
        matitahun.plot(x = 'Year', y='Count', kind='scatter')
        plt.show()
        # print(matitahun["Year"].value_counts(["Year"]).reset_index(name="Count"))
        # matitahun["Year"].value_counts()

def deadstate():
        matistate = police[["State"]].value_counts(["State"]).reset_index(name='Count')
        print(matistate)
        matistate.plot(x = 'State', y='Count', kind='scatter')
        plt.show()

def deadreason():
        matireason = police[["Cause_of_Death"]].value_counts(["Cause_of_Death"]).reset_index(name='Count')
        # matireason = matireason.loc[(matireason["Cause_of_Death"] != "Gunfire")]
        print(matireason)
        # matireason.plot(x = 'CauseOfDeath', y='Count', kind='scatter')
        # plt.show()

def deaddept():
        matidept = police[["Department"]].value_counts(["Department"]).reset_index(name='Count')
        print(matidept)
        # matidept.plot(x='Department', y='Count', kind='scatter')
        # plt.show()


print(" ")
namaanda = input("Masukkan nama anda : ")

while True:
    
    print(" ")
    print("Selamat datang di pusat informasi Kepolisian Amerika Serikat, "+namaanda.title())
    print(" ")
    print("Informasi apa yang anda butuhkan, silahkan pilih salah satu :")
    print("1. Jumlah kematian per tahun")
    print("2. Jumlah kematian per daerah")
    print("3. Jumlah penyebab kematian")
    print("4. Jumlah kematian per departemen")
    print("5. Variance Data Information")
    print("6. Standard Deviation Data Information")
    print("7. Probability Distribution Data Information")
    print(" ")
    pilihan = input("Pilihan anda no : ")

    if pilihan.lower() == "1":
        print("Informasi jumlah kematian per tahun : ")
        # mean()
        deadyear()
        print(" ")
        ulang = input("Apakah anda ingin kembali ke menu utama ? (Ya/Tidak) : ")
        if ulang.lower() == "tidak":
            break

    if pilihan.lower() == "2":
        print("Informasi jumlah kematian per daerah")
        # median()
        deadstate()
        print(" ")
        ulang = input("Apakah anda ingin kembali ke menu utama ? (Ya/Tidak) : ")
        if ulang.lower() == "tidak":
            break

    if pilihan.lower() == "3":
        print("Informasi jumlah penyebab kematian")
        # modus()
        deadreason()
        print(" ")
        ulang = input("Apakah anda ingin kembali ke menu utama ? (Ya/Tidak) : ")
        if ulang.lower() == "tidak":
            break

    if pilihan.lower() == "4":
        print("Informasi jumlah kematian per departement")
        # range()
        deaddept()
        print(" ")
        ulang = input("Apakah anda ingin kembali ke menu utama ? (Ya/Tidak) : ")
        if ulang.lower() == "tidak":
            break

    if pilihan.lower() == "5":
        print("Pilihan 5")
        variance()
        print(" ")
        ulang = input("Apakah anda ingin kembali ke menu utama ? (Ya/Tidak) : ")
        if ulang.lower() == "tidak":
            break

    if pilihan.lower() == "6":
        print("Pilihan 6")
        std()
        print(" ")
        ulang = input("Apakah anda ingin kembali ke menu utama ? (Ya/Tidak) : ")
        if ulang.lower() == "tidak":
            break

    if pilihan.lower() == "7":
        print("Pilihan 7")
        prob()
        print(" ")
        ulang = input("Apakah anda ingin kembali ke menu utama ? (Ya/Tidak) : ")
        if ulang.lower() == "tidak":
            break
