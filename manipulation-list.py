## Operation

#! index 0(-3)  1(-2)  2(-1)
data = ["ucup","momon","turu"]

#? mengambil data dari list atas
data_0 = data[0]
data_1 = data[1]
data_2 = data[2]
print (f"data pertama (index 0) = {data_0}")
print (f"data pertama (index 1) = {data_1}")
print (f"data pertama (index 2) = {data_2}")

data_terakhir = data[-1]
print (f"data terakhir adalah = {data_terakhir}")

#? mengambil info jumlah data dalam list 
panjang_data = len(data)
print (f"panjang data = {panjang_data}")



## Manipulation data list

#? menambahkan item pada list sesuai posisi
print (f"Data sebelum ditambahkan = \n{data}")

#! data.insert(posisi, item)
data.insert(1, "Coy")
print (f"Data sesudah ditambahkan = \n{data}")

#? menambahkan diakhir list 
data.append("coeg")
print (f"Data ditambahkan diakhir = \n{data}")

#? mengabungkan list dengan list 
data_baru = ["momon","coy","dudung"]
data.extend(data_baru)
print (f"Data gabungan = \n{data}")

#? merubah data pada list
data[2] = "Jordan"
print (f"Data diubah = \n{data}")

#? menghapus data pada list 
data.remove("turu")
print (f"Data dihapus = \n{data}")

#? menghapus data paling belakang
data.pop()
print (f"Data akhir dihapus = \n{data}")