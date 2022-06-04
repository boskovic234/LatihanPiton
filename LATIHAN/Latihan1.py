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

#coba

uang = int(input("Masukkan uang anda :"))
#uang = int(uang)

hargabuku = int(input("Masukkan harga buku:"))
#hargabuku = int(hargabuku)

totalbeli = int(input("Mau beli berapa :"))
#totalbeli = int(totalbeli)

totalbelanja = hargabuku * totalbeli

if uang < totalbelanja:
    print ("Uang Anda Kurang")

if uang >= totalbelanja:
    print ("Berhasil Checkout")
    uang = str(uang - totalbelanja)
    #uang = str(uang)
    print ("Sisa Uang Anda Adalah :" + uang)
