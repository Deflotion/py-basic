'''function with return'''

#! template function dengan return
#* def nama_fungsi(argument):
#*      badan fungsi
#*      return output

#? function kuardrat

def kuadrat(input_angka):
    output = input_angka**2 
    return output

y = kuadrat(5)
print(y)

print(kuadrat(6))

z = 23 + 21 - 34 + kuadrat(7)
print(z)


#? function tambah
def fungsi_tambah(angka_1,angka2):
    #$ fungsi return dengan multi inpout
    return angka_1 + angka2

a = fungsi_tambah(65,15)
print(a)

#? function dengan return banyak
def operasi_mat(angka_1,angka_2):
    kali = angka_1 * angka_2
    bagi = angka_1 / angka_2
    kurang = angka_1 - angka_2
    tambah = angka_1 + angka_2
    return kali,bagi,kurang,tambah

k,l,m,n = operasi_mat(9,5)

print(f"Hasil kali = {k}")
print(f"Hasil bagi = {l}")
print(f"Hasil kurang = {m}")
print(f"Hasil tambah = {n}")