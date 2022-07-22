
#! function dengan arguments (input)
#$ def = definitional 
#$ setelah def adalah nama dari function tersebut baru (:) dan bodynya
#$ contoh 
''' 
def nama_fungsi(argument): 
    badan fungsi
'''

def hello_world(nama):
    print(f"Selamat datang didunia {nama}")

hello_world("ucup")

#* program tambah
def tambah(angka_1,angka_2):
    #? function tambah
    hasil = angka_1 + angka_2
    print(f"{angka_1} + {angka_2} = {hasil}")

tambah(2,5)
tambah(3500000,20)

def awikwok(list_nama):
    data_orang = list_nama.copy()
    for nama in data_orang:
        print(f"Nama anda adalah {nama}")
    
anggota = ["Ujang","Ucup","Aawok"]
awikwok(anggota)