import numpy as np

list_a = [1,2,3,4] #? muncul koma dan tidak bisa di buat proses aritmatika
vector_a = np.array([1,2,3,4]) #? koma hilang dan bisa dibuat proses aritmatika cocok utk matriks


print(f"list a = {list_a}")


print(f"vector a = {vector_a}")
print(f"a pangkat 2 = {vector_a**2}")
print(f"a kali 5 = {vector_a*5}")

matriks_a = np.array([(1,2),(3,4)])
matriks_b = np.array([(5,6),(1,2)])
print(f"matriks a = \n{matriks_a}")
print(f"matriks b = \n{matriks_b}")
print(f"matriks a^2 = \n{matriks_a**2}")
print(f"matriks a*b = \n{matriks_a*matriks_b}")

zeros_c = np.zeros((2,2))
print(f"zeros_c = \n{zeros_c}")

ones_d = np.ones((2,2))
print(f"ones_d = \n{ones_d}")

#? proses penjumlahan matriks
jumlah = matriks_a + matriks_b + ones_d + matriks_a**3
print(f"Jumlah = \n{jumlah}")