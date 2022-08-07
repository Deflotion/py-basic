## Global dan Local Scope

nama_global = "Otong" #$ <-variable global

#? akses variable global dalam fungsi
def fungsi1():
    print(f"fungsi menampilkan {nama_global}")

fungsi1()

#? akses variable global dalam loop
for i in range(0,5):
    print(f"loop{i}->{nama_global}")

#? percabangan
if True:
    print(f"if menampilkan {nama_global}")


## Variable Local Scope
def fungsi2():
    nama_local = "Ucup" #$ <-variable local

fungsi2()
#$ print(nama_local) <- tidak bisa dilakukan


#& contoh 1: penggunaan akses variable 
def say_otong():
    print(f"Hello {nama}")

nama = "Ucup"
say_otong()

#& contoh 2: merubah variable global
angka = 0
name = "Ucup"
def ubah(angka_baru,nama_baru):
    global angka #? function ini mendapat akses merubah secara global
    global name
    angka = angka_baru
    name = nama_baru

print(f"Sebelum {angka,name}")
ubah(100,"awikwok")
print(f"Sesudah {angka,name}")

#& contoh 3: 
angka = 0

for i in range(0,5):
    angka += i
    angka_dummy = 0

print(angka)
print(angka_dummy)

if True:
    angka = 20
    angka_dummy = 40
print(angka)
print(angka_dummy)

