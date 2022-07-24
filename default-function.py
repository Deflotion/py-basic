'''Default Argument'''

#$ def fungsi(argument):
#$ def fungsi(argument = nilai defaultnya):


#? contoh 1
def say_hello(nama = "World"):
    '''function dengan default argument'''
    print(f"Hello,{nama}")

say_hello("Ujang")
say_hello()

#? contoh 2
def sapa_dia(nama,pesan = "Apa kabar?"):
    '''function dengan 1 input biasa, dengan satu default argument'''
    print(f"Hi {nama}, {pesan}")

sapa_dia("Kimi","Hello World")
sapa_dia("Ucup")

#? contoh 3
def hitung_pangkat(angka,pangkat=2):
    hasil = angka**pangkat
    return hasil

print(hitung_pangkat(2))
print(hitung_pangkat(7,3))
print(hitung_pangkat(pangkat = 3,angka = 4))

#? contoh 4 berfungsi jika argumentnya banyak
def fungsi(input1=2,input2=4,input3=6,input4=8):
    hasil = input1+ input2+input3+input4
    return hasil

print(fungsi())
#$ bisa merubah salah 1 argument dengan mengakses argument yg ingin diubah
print(fungsi(input3=9))