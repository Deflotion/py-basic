
#? package adalah sebuah program/tempat untuk menaruh module-module

import sains.mat
from sains import fisika
from sains.fisika import gaya as gy


hasil_tambah = sains.mat.tambah(1,2,3,1,3)
print(f"hasil tambah dari package = {hasil_tambah}")

gaya = fisika.gaya(40,22)
print(f"hasil gaya = {gaya}")

gaya = gy(40,22)
print(f"hasil gaya = {gaya}")