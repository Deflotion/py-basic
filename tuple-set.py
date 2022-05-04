
#? list
#* menggunakan kurung []
data_list = [1,2,3,4,5]
print(data_list)

#? tuples
#* menggunakan kurung ()
#* kekurangannya tidak bisa diubah isinya/fix
#* tidak support append
#* berfungsi untuk membuat suatu data akhir supaya tidak bisa diubah,data constan
data_tuples = (1,2,4,3,5)
print(data_tuples)
print(data_tuples[1])

#* tidak bisa
#$ data_tuples[1] = "momon"
#$ data_tuples.append(1)


#? sets (himpunan)
#* sebuah collection yang tidak mempunyai index,hanya untuk menghitung data saja
#* command lainnya bisa kecuali memanggil index
data_sets = {1,2,3,4,5,6}
print(data_sets)

#* tidak bisa
#$ print(data_sets[1])