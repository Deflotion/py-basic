'''**kwargs'''

def fungsi(nama,tinggi,berat):
    #& function biasa
    print(f"{nama} mempunya tinggi {tinggi} dan berat {berat}")

fungsi("Ucok",123,54)

#cat memberi function dengan mengunakan keyword
#cat dan menggunakan (**) didepan nama argument
#cat mengambil data berupa dictionary
def fungsi(**kwargs):
    #& function kwargs
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]
    print(f"{nama} mempunya tinggi {tinggi} dan berat {berat}")

fungsi(nama="Ucok",tinggi=123,berat=54)

#$ studi kasus
def math(*args,**kwargs):
    output = 0
    if kwargs["option"] == "tambah":
        for angka in args:
            output += angka
    elif kwargs["option"] == "kali":
        output = 1
        for angka in args:
            output *= angka
    else:
        print("Tidak ada operasi")
    return output

hasil = math(1,2,3,4,option="tambah")
print(f"Hasil jumlah = {hasil}")
hasil = math(1,2,3,4,option="kali")
print(f"Hasil kali = {hasil}")

