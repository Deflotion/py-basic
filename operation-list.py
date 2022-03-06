## Operasi list ke-2

data_angka = [1,2,4,3,4,5,2,3,2,4,3,2,6,4,2,6,5,7,6,3,4,2,4,2,3,2]
print (f"data angka = \n{data_angka}")

#? count data 
jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)
print (f"jumlah data 4 = {jumlah_data_4}")
print (f"jumlah data 3 = {jumlah_data_3}")

#? ambil posisi data
data = ["ucup","momon","turu","jordan"]
print (f"data = {data}")

index_momon = data.index("momon")
index_turu = data.index("turu")
print (f"index momon = {index_momon}")
print (f"index turu = {index_turu}")

#? mengurutkan list data
#*mengurutkan data angka
print (f"data angka sebelum disort = \n{data_angka}")
data_angka.sort()
print (f"data angka sesudah disort = \n{data_angka}")

#* mengurutkan data string
print (f"data sebelum disort = \n{data}")
data.sort()
print (f"data sesudah disort = \n{data}")

#? reverse list
data_angka.reverse()
data.reverse()
print (f"data yang direverse = \n{data_angka} \n{data}")