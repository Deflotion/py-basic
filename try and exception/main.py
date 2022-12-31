
#? exception akan terjadi saat program mengalami error saat runtime

#$ contoh sederhana untuk menangkap exception

from math import nan

#* contoh sederhana penggunaan try and catch
# user_input = int(input("Masukan angka: "))
# hasil = nan

# try:
#     hasil = 10/user_input
# except:
#     print("Inputan anda salah")

# print(f"Hasil = {hasil}")

#* contoh di aplikasi 1
while(True):
    angka = int(input("Masukan angka: "))
    try:
        hasil = 10/angka
        print(f"Hasil = {hasil}")
        isdone = input("Ingin lanjut(y/n)? ")
        if isdone == 'n':
            break
    except:
        print("Input anda salah")
print("Akhir program 1")

#* contoh aplikasi untuk membuat file data.txt dgn try and catch
try:
    with open("try and exception/data_txt",'r') as file:
        print(file.read())
except:
    print("File tidak tersedia, membuat data.txt")
    with open("try and exception/data_txt",'w',encoding='utf-8') as file:
        file.write("file baru")
print("Akhir program 2")