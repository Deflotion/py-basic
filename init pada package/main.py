
#? fungsi init untuk langsung mengeksekusi saat import packagenya 
import sains
from sains.mat import scientific


hasil_tambah = sains.mat.tambah(2,3,1,4)
print(f"hasil tambah = {hasil_tambah}")

hasil_gaya = sains.fisika.gaya(20,65)
print(f"hasil gaya = {hasil_gaya}")

hasil_kali = sains.mat.kali(2,5,2,3)
print(f"hasil gaya = {hasil_kali}")

pangkat3 = scientific.pangkat(2)
print(f"hasil pangkat = {pangkat3(3)}")

# from sains import *

# hasil_tambah = mat.basic.tambah(2,3,1,4)
# print(f"hasil tambah = {hasil_tambah}")

# hasil_gaya = fisika.gaya(20,65)
# print(f"hasil gaya = {hasil_gaya}")

# hasil_kali = mat.basic.kali(2,5,2,3)
# print(f"hasil gaya = {hasil_kali}")