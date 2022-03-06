## nested list

data_0 = [1,2]
data_1 = [3,4,5]

data_list_biasa = [1,2,3,4]
print (f"Data list biasa = {data_list_biasa}")

list_2D = [data_0, data_1,6,7]
print (f"Data list 2D = {list_2D}")

#? contoh pengunaan nested list
peserta_0 = ["ucup",20,"Laki-laki"]
peserta_1 = ["momon",23,"Laki-laki"]
peserta_2 = ["turu",25,"Wanita"]

list_peserta = [peserta_0,peserta_1,peserta_2]
print (f"list peserta = \n{list_peserta}\n")

for peserta in list_peserta:
    print (f"nama\t : {peserta[0]}")
    print (f"umur\t : {peserta[1]}")
    print (f"gender\t : {peserta[2]}\n")

#! masalah dengan reference
list_copy = list_peserta.copy() #! hanya mengcopy bagian luarnya saja (list_peserta) bagian (peserta_0) tidak tercopy
print (f"list peserta = \n{list_copy}")
peserta_0[0] = "usep" 
print (f"list peserta = \n{list_copy}")
print (f"list peserta = \n{list_peserta}")