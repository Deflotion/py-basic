## ---LIST---

#* Kumpulan data Int
data_angka = [1,2,3,4]
print (data_angka)

#* Kumpulan data String]
data_string = ["test","momon","xixixi"]
print (data_string)

#* Kumpulan data Boolean
data_boolean = [True,False,False,False]
print (data_boolean)

#* Kumpulan data Campuran
data_campuran = [1,2,3,4,"test","momon",True,False]
print (data_campuran)

#? cara alternatif membuat list
data_range = range(0,10,2) #! range(Start,Stop,Step)
print (data_range)
data_list = list(data_range)
print (data_list)

#* Membuat list dengan For loop, list comprehension
data_list_for = [i for i in range(0,10)]
print (data_list_for)

#! list kuadrat
data_list_for = [i**2 for i in range(0,10)]
print (data_list_for)

#* Membuat list dengan For dan If
list_for_if = [i for i in range(0,10) if i != 8]
print (list_for_if)

#! menentukan genap
list_for_if = [i for i in range(0,10) if i%2 == 0]
print (list_for_if,"ini genap")

#! menentukan ganjil
list_for_if = [i for i in range(0,10) if i%2 != 0]
print (list_for_if,"ini ganjil")