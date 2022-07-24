'''Latihan Function'''

import os


#? program untuk menghitung luas dan keliling persegi panjang

#! cara panjang
#? membuat header program
# while True:
#     os.system("cls")
#     print(f"{'Program hitung Luas':^40}")
#     print(f"{'dan Keliling Persegi Panjang':^40}")
#     print(f"{'-'*40:^40}")

#     #? Mengambil input User
#     PANJANG = int(input("Masukan Nilai Panjang: "))
#     LEBAR = int(input("Masukan Nilai Lebar: "))

#     #? program hitung luas
#     LUAS = PANJANG*LEBAR
#     KELILING = 2*(PANJANG+LEBAR)

#     #? output hasil
#     print(f"Hasil Luas     = {LUAS}") 
#     print(f"Hasil Keliling = {KELILING}")


#! mengunakan function dan rapi

def header():
    '''Function Header'''
    os.system("cls")
    print(f"{'Program hitung Luas':^40}")
    print(f"{'dan Keliling Persegi Panjang':^40}")
    print(f"{'-'*40:^40}")

def pilih():
    print("Pilih metode perhitungan: ")
    print("1.Keliling")
    print("2.Luas")

def input_user():
    '''Function user input'''
    lebar = int(input("Masukan Nilai Lebar: "))
    panjang = int(input("Masukan Nilai Panjang: "))
    return lebar,panjang

def hitung_luas(lebar,panjang):
    return lebar*panjang

def hitung_keliling(lebar,panjang):
    return 2*(panjang+lebar)

def output(message,value):
    '''function display'''
    print(f"Hasil Perhitungan {message} = {value}")

#? program utama
while True:
    header()
    pilih()
    opsi = input("Pilih Metode No: ")
    if opsi == "1":
        LEBAR,PANJANG = input_user()
        KELILING = hitung_keliling(LEBAR,PANJANG)
        output("Keliling",KELILING)

    else:
        LEBAR,PANJANG = input_user()
        LUAS = hitung_luas(LEBAR,PANJANG)
        output("Luas",LUAS)

    #? logika looping
    isContinue = input("Apakah mau lanjut(y/n) ? ")
    if isContinue == "n":
        break
print("Program selesai,Terima kasih")