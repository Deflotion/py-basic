# angka = float(input('Masukan angka: '))
# celcius = angka - 273
# fahrenheit = ((9/5)*celcius) + 32
# print (fahrenheit,"F")

# celcius1 = 9/5*(angka - 32)
# kelvin1 = celcius1 + 273
# print(kelvin1,"K")

# inputuser = float(input("masukan angka: "))
# isLebihDari = inputuser > 0
# isKurangDari = inputuser < 5
# isLebihDari1 = inputuser > 8
# isKurangDari1 = inputuser < 11
# isCorrect = isLebihDari and isKurangDari or isKurangDari1 and isKurangDari1
# print("hasilnya adalah", isCorrect) 

# inputuser = float(input("masukan angka: "))
# isLebihDari = inputuser < 0
# isKurangDari = inputuser > 5
# isLebihDari1 = inputuser < 8
# isKurangDari1 = inputuser > 11
# isCorrect = isLebihDari or isKurangDari and isKurangDari1 or isKurangDari1
# print("hasilnya adalah", isCorrect) 


# x = float(input("\nMasukkan angka: "))
# y = 0 < x < 5 or 8 < x < 11
# print("Status angka: ",y)

# x = float(input("\nMasukkan angka: "))
# y = 0 > x or 5 < x < 8 or x > 11
# print("Status angka: ",y)


#! Date and time
# ?import datetime as dt
# tgl = dt.date.today()
# print(tgl)
# print("Masukan tanggal:")
# tanggal = int(input("Tanggal \t:"))
# bulan = int(input("Bulan \t\t:"))
# tahun = int(input("Tahun \t\t:"))
# tgl = dt.date(tahun,bulan,tanggal)
# print(f"Tanggal lahir anda: {tgl}")
# print(f"Harinya adalah: {tgl:%A}")

# hari_ini = dt.date.today()
# print(f"hari ini tanggal: {hari_ini}")
# umur_hari = hari_ini - tgl
# umur_bulan = (umur_hari.days % 365) // 30
# umur_tahun = umur_hari.days // 365
# print(f"umur anda adalah {umur_hari}")
# print(f"umur anda adalah {umur_tahun} tahun {umur_bulan} bulan")


# * if else elif
# nama = input("Nama anda? ")

# if  nama == "jancuk":
#     print("halo jancuk")
# elif nama == "panteq":
#     print("halo panteq")
# else:
#     print("ah ga asik")

# !kalkulator
# print(20*"=")
# print("Kalkulator")
# print(20*"=")

# angka_1 = float(input("Masukan angka 1  : "))
# operator = input("Masukan Operator : ")
# angka_2 = float(input("Masukan angka 2  : "))

# if operator == "+":
#     hasil = angka_1 + angka_2
#     print(f"Hasilnya adalah {hasil}")
# elif operator == "-":
#     hasil = angka_1 - angka_2
#     print(f"Hasilnya adalah {hasil}")
# elif operator == "*":
#     hasil = angka_1 * angka_2
#     print(f"Hasilnya adalah {hasil}")
# elif operator == "/":
#     hasil = angka_1 / angka_2
#     print(f"Hasilnya adalah {hasil}")
# else :
#     print("Masukin yang bener goblog")


# !for looping
# for i in range(10):
#     print(f"ini adalah angka {i}")  

#! while looping
# angka = float(input("masukan angka "))

# while angka < 10:
#     angka += 1
#     print("gas lah ampe habis")

#! sort
# n = 0
# angka = eval(input("masukan angka: "))
# print("Angka awal adalah ", angka)
# while angka < n:
    
# angka.sort()
# print("Angka ascending ",angka)
# angka.sort(reverse=True)
# print("Angka descending ",angka)

#! testing
# a = ["al", "au", "ha", "ut", "ak", "lo"]
# for i in range(4):
#     a[i]= a[i].strip("a")
#     print(a[i],end='')

#! fibonaci
# n = int(input("Masukan angka: "))
# d1 = 0
# d2 = 1
# for i in range(n):
#     print(d1, end=' ')
#     rumus = d2 + d1 
#     d1 = d2
#     d2 = rumus 

#! buble sort
#* cara 1
# def bubblesort(data):
#     for i in range(len(data)-1,-1,-1):
#         for j in range(i):
#             if data[j] > data[j+1]:
#                 temp = data[j]
#                 data[j] = data[j+1]
#                 data[j+1] = temp
#                 print (data)

# data = [2,4,1,5,3]
# bubblesort(data)
# print ("###########")
# print(data)

#* cara 2
# import numpy 
# def bubblesort(array_sort, reverse=False):
#     if reverse:
#         n=len(array_sort)
#         for i in range(n):
#             for j in range(0,n-i-1):
#                 if array_sort[j]>array_sort[j+1]:
#                     array_sort[j],array_sort[j+1] = array_sort[j+1],array_sort[j]
#     else:
#         n=len(array_sort)
#         for i in range(n):
#             for j in range(0,n-i-1):
#                 if array_sort[j]<array_sort[j+1]:
#                     array_sort[j],array_sort[j+1] = array_sort[j+1],array_sort[j]



# import numpy 
# my_data = numpy.empty(10)
# for i in range(10):
#     x = float(input("Angka:"))
#     my_data[i] = x
# bubblesort(my_data)
# print (my_data)


#! membuat segitiga
#* cara 1
# n = int(input("Masukan angka: "))
# for i in range(n):
#     for j in range(i+1):
#         print ("X",end="")
#     print ()

#* cara 2
# n = int(input("Masukan angka: "))
# for i in range(n+1):
#     print ("X"*i)


#! tutle color
# import turtle
# a = 0
# b = 0

# turtle.bgcolor()
# turtle.speed()
# turtle.pencolor()
# turtle.penup()

