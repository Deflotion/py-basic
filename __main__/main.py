
#? __main__ adalah top level code environment

#? __name__ == "__main__" akan terjadi jika dipanggil dalam program utama

#$ __name__ pada program file utama
print(f"Nilai __name__ pada main.py = '{__name__}'")

#$ __name__ pada program file eksternal
import fungsi

#$ contoh penggunaan __main__
#* deklarasi
def tambah(a:int,b:int)->int:
    return a+b

#* fungsi utama
if __name__ == "__main__":
    angka1 = 10
    angka2 = 5
    hasil = tambah(angka1,angka2)
    print(f"Hasil tambah = {hasil}")

#$ mencoba memanggil package
import package