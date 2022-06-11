import numpy as np

# Latihan function
# ---------------------
# x = 5
# y = 2

# def fungsi(x,y):
#     print (x*y)

# fungsi(x,y)


# # Function untuk melempar string
# def printme( str ):
# #    "This prints a passed string into this function"
#    print(str)
#    return;

# # Now you can call printme function
# printme("I'm first call to user defined function!")
# printme("Again second call to the same function")

# # Function definition is here
# def changeme( mylist ):
#    "This changes a passed list into this function"
#    mylist.append(1);
#    mylist.append(2);
#    mylist.append(3);
#    print("Values inside the function: ", mylist)
#    return

# # Now you can call changeme function
# mylist = [10,20,30];
# changeme( mylist );
# print("Values outside the function: ", mylist)



# jumlahKucing = 20

# def jumlahHewan():
#     jumlahAnjing = 30
#     return jumlahKucing + jumlahAnjing

# def jumlahKelinci():
#     return jumlahKucing + jumlahKucing

# jumlahHewan()
# jumlahKelinci()


# ---------------------------
# print (np.version.version)

# a = np.array([1,2,3,4,5])
# a = np.append(a, [6,7])
# print (a)

# a = np.delete(a, 1)
# print (a)


# b = np.zeros(5)
# print (b)

# -------------------------
# data = np.array([1,2,3,4,5])

# print(data)
# print(data[0])
# print(data[1])
# print(data[0:3])
# print(data[1:]) #mengambil data seluruhnya setelah index/array tsb
# print(data[-2:])

# ----------------------------------
arr = np.array([[1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12],
                     [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]])

arr = np.hsplit(arr, 2)

print (arr)