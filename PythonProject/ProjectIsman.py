import numpy as np
import pandas as pd

nycdata = pd.read_csv("nyc-rolling-sales.csv")

# Untuk cek data berhasil di load
# print(nycdata.head(10))

# untuk compile 
# python -m py_compile namafile.py

# print(nycdata.info())
# print(nycdata.describe())


## -------------------------------BATAS
def mean():
    print("Memanggil Function Mean")

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

print(" ")
namaanda = input("Masukkan nama anda : ")

while True:
    
    print(" ")
    print("Selamat datang di pusat informasi property New York, "+namaanda.title())
    print(" ")
    print("Informasi apa yang anda butuhkan, silahkan pilih salah satu :")
    print("1. Mean Data Information")
    print("2. Median Data Information")
    print("3. Modus Data Information")
    print("4. Range Data Information")
    print("5. Variance Data Information")
    print("6. Standard Deviation Data Information")
    print("7. Probability Distribution Data Information")
    print(" ")
    pilihan = input("Pilihan anda no : ")

    if pilihan.lower() == "1":
        print("Pilihan 1")
        mean()
        print(" ")
        ulang = input("Apakah anda ingin kembali ke menu utama ? (Ya/Tidak) : ")
        if ulang.lower() == "tidak":
            break

    if pilihan.lower() == "2":
        print("Pilihan 2")
        median()
        print(" ")
        ulang = input("Apakah anda ingin kembali ke menu utama ? (Ya/Tidak) : ")
        if ulang.lower() == "tidak":
            break

    if pilihan.lower() == "3":
        print("Pilihan 3")
        modus()
        print(" ")
        ulang = input("Apakah anda ingin kembali ke menu utama ? (Ya/Tidak) : ")
        if ulang.lower() == "tidak":
            break

    if pilihan.lower() == "4":
        print("Pilihan 4")
        range()
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
