import datetime
import os
#? import untuk membuat key acak
import string
import random
#* fromkeys

#! membuat aplikasi sederhana mengunakan dict
#$ template dict mahasiswa

template_mahasiswa = {
    'nama':'nama',
    'nim':'00000000',
    'sks_lulus':0,
    'lahir':datetime.datetime(1111,1,11)
}

data_mahasiswa = {}

#? biar looping terus 
while True:
    os.system("cls")
    print(f"{'SELAMAT DATANG':^20}")
    print(f"{'DATA MAHASISWA':^20}")
    print("-"*20)

    mahasiswa = dict.fromkeys(template_mahasiswa.keys())

    mahasiswa['nama']  = input("Nama Mahasiswa : ")
    mahasiswa['nim']   = input("Nim Mahasiswa  : ")
    mahasiswa['sks_lulus']   = int(input("SKS Mahasiswa  : "))
    TAHUN_LAHIR = int(input("Tahun lahir (YYYY): "))
    BULAN_LAHIR = int(input("Bulan lahir (1-12): "))
    TANGGAL_LAHIR = int(input("Tanggal lahir (1-31): "))
    mahasiswa['lahir'] = datetime.datetime(TAHUN_LAHIR,BULAN_LAHIR,TANGGAL_LAHIR)

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_mahasiswa.update({KEY:mahasiswa})

    #? dari tutorial nesting hanya saja beasiswa dihapus
    print(f"\n{'KEY':<6} {'Nama':<15} {'NIM':<8} {'SKS Lulus':<10} {'Tanggal Lahir':<10}")
    print("-"*60)
    
    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa
        
        NAMA = data_mahasiswa[KEY]['nama']
        NIM = data_mahasiswa[KEY]['nim']
        SKS =  data_mahasiswa[KEY]['sks_lulus']
        LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x") 
        print(f"{KEY:<6} {NAMA:<15} {NIM:<8} {SKS:^10} {LAHIR:^10}")
        
    print("\n")
    is_done = input("Ingin melanjutkan (y/n)? ")
    if is_done == "n":
        break

print("\nSudah selesai terima kasih")