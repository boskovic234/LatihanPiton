from ast import operator
import statistics as stat
import string

#nilaimean = stat.mean([1,2,3,4,5,6,7,8])
#nilaimedian = stat.median([2,3,4,5,6,7,8,9,5,4])

#dirubah


#alas = int(input("Nilai alas :"))
#tinggi = int(input("Nilai tinggi :"))

#luas = (alas*tinggi)/2

#print(luas)

#a = ('aab')
#b = ('cungu')
#c = 1

#c = str(c)

#print(a+b+c)


#LATIHAN 1

# uang = int(input("Masukkan uang anda :"))
# #uang = int(uang)

# hargabuku = int(input("Masukkan harga buku:"))
# #hargabuku = int(hargabuku)

# totalbeli = int(input("Mau beli berapa :"))
# #totalbeli = int(totalbeli)

# totalbelanja = hargabuku * totalbeli

# if uang < totalbelanja:
#     print ("Uang Anda Kurang")

# if uang >= totalbelanja:
#     print ("Berhasil Checkout")
#     uang = str(uang - totalbelanja)
#     #uang = str(uang)
#     print ("Sisa Uang Anda Adalah :" + uang)


#LATIHAN 2
nilaiabsen = int(input("Masukkan Nilai Absen :"))
nilaitugas = int(input("Masukkan Nilai Tugas :"))
nilaiuts = int(input("Masukkan Nilai UTS :"))
nilaiuas = int(input("Masukkan Nilai UAS :"))

nilaiabsen = nilaiabsen * 0.1
nilaitugas = nilaitugas * 0.2
nilaiuts = nilaiuts * 0.3
nilaiuas = nilaiuas * 0.4

nilaiakhir = nilaiabsen + nilaitugas + nilaiuts + nilaiuas

if (nilaiakhir > 80) and (nilaiakhir <= 100):
    print(nilaiakhir)
    print("Grade Anda A")

elif (nilaiakhir > 70) and (nilaiakhir <= 80):
    print(nilaiakhir)
    print("Grade Anda B")

elif (nilaiakhir > 60) and (nilaiakhir <= 70):
    print(nilaiakhir)
    print("Grade Anda C")

elif (nilaiakhir > 50) and (nilaiakhir <= 60):
    print(nilaiakhir)
    print("Grade Anda D")

elif (nilaiakhir < 50 ):
    print(nilaiakhir)
    print("Grade Anda E")