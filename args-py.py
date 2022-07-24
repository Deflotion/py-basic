'''*args'''

#$ memasukan argument secara biasa dan menggunakan list
def fungsi(nama,tinggi,berat):
    print(f"{nama} mempunyai tinggi {tinggi} dan berat {berat}")

fungsi("Ucok",150,70)

def fungsi(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"{nama} mempunyai tinggi {tinggi} dan berat {berat}")

fungsi(["Ucok",200,80])

#! perkenalan dengan *args
#? tidak wajib menggunakan *args
#? intinya menggunakan (*) diawalan nama contoh *data
def fungsi(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} mempunyai tinggi {tinggi} dan berat {berat}")

fungsi("Dodo",240,70)

#$ studi kasus
def tambah(*data):
    #& tipe data tuple
    output = 0
    for angka in data:
        output += angka
    return output

hasil = tambah(1,23,4,2,53,2)
print(f"Hasilnya = {hasil}")
hasil = tambah(1,2,5,2)
print(f"Hasilnya = {hasil}")