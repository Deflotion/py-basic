
#! Lambda function
#$ berfungsi membuat program function menjadi simple
#$ penggunaannya membuat variable lalu setelah (=) diawali lambda function
#$ contoh template 
#$  nama_variable = lambda nama_argument:ekspresi

#* contoh tanpa lambda function
def f_kuadrat(angka):
    return angka**2
print(f"Hasil Funsgi kuadrat = {f_kuadrat(3)}")

#* contoh menggunakan lambda function
kuadrat = lambda angka:angka**2

print(f"Hasil Lambda kuadrat = {kuadrat(5)}")

#? menggunakan 2 input
pangkat = lambda num,pow:num**pow
print(f"Hasil Lambda pangkat = {pangkat(3,4)}")

#$ kegunaan lambda function
#$ sort untuk list biasa
data_list = ["Otong","Ucup","Dudung"]
data_list.sort()
print(f"Sorted list = {data_list}")

#$ sorting berdasarkan panjang kata
def panjang_nama(nama):
    return len(nama)
data_list.sort(key=panjang_nama)
print(f"Sorted list by len = {data_list}")

#$ sort pakai lambda
data_list = ["Otong","Ucup","Dudung"]
data_list.sort(key = lambda nama:len(nama))
print(f"Sorted list by lambda = {data_list}")

#$ filter
data_list = [1,2,3,4,5,6,7,8,9,10,11,12]

def angka_kurang_lima(angka):
    return angka<5

data_list_baru = list(filter(angka_kurang_lima, data_list))
data_list_baru = list(filter(lambda x:x<7,data_list))
print(data_list_baru)

#$ kasus genap
data_genap = list(filter(lambda x:(x%2==0),data_list))
print(data_genap)

#$ kasus ganjil
data_ganjil = list(filter(lambda x:(x%2!=0),data_list))
print(data_ganjil)

#$ kasus kelipatan 3
data_kelipatan_3 = list(filter(lambda x:(x%3==0),data_list))
print(data_kelipatan_3)


#! anonymous function
#$ currying <- Haskell Curry (pencipta bahasa Huskell)

def pangkat(angka,n):
    hasil = angka**n
    return hasil

data_hasil = pangkat(5,2) 
print(f"Hasil pangkat = {data_hasil}")

#$ dengan currying menjadi
def pangkat(n):
    return lambda angka:angka**n

pangkat2 = pangkat(2)
print(f"Hasil pangkat 2 = {pangkat2(4)}")
pangkat3 = pangkat(3)
print(f"Hasil pangkat 3 = {pangkat3(5)}")
print(f"Hasil pangkat bebas = {pangkat(2)(5)}")