
#! module matematika dengan import 

from matematika import tambah as add
from matematika import kali as kl
from matematika import pangkat as pk
# from matematika import *

import matematika as math #? <-- bisa dilakukan 

hasil_tambah = add(3,2,5,7,1,4)
hasil_kali = math.kali(2,3,4,2,1,5)
hasil_pangkat = pk(2)

print(f"Hasil tambah = {hasil_tambah}")
print(f"Hasil kali = {hasil_kali}")
print(f"Hasil pangkat = {hasil_pangkat(5)}")