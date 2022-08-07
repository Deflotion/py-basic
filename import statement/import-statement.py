
#! import
#? fungsinya untuk mengambil program dari file eksternal .py

#$ 1. untuk menyambung program dari eksternal dan menjalankan
import program_test
import program_ucup

#$ 2. import dengan data
import variable
import coeg

#* data ada dinamespace variable
print(variable.data)
print(coeg.data)

#$ 3. import dengan function 
import matematika
hasil = matematika.tambah(4, 6)
print(f"hasil tambah {hasil}")