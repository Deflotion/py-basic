
#! tutorial membaca file eksternal

print(5*"=","Membaca file txt",5*"=")
file = open("read file eksternal/file.txt",mode="r")

print(f"Status read = {file.readable()}")
print(f"Status write = {file.writable()}")

#cat baca seluruh baris
print(file.read())

#cat baca perbaris
#print(file.readline(),end="") #* baca baris pertama
#print(file.readline(),end="") #* baca baris kedua

#cat baca seluruh baris sebagai baris
#print(file.readlines()) 

print(f"Apakah file sudah diclose = {file.closed}")
file.close()
print(f"Apakah file sudah diclose = {file.closed}")

#$ salah satu teknik membuka file dipy
print(5*"=","Membaca file txt dengan with",5*"=")
with open("read file eksternal/file.txt",mode="r") as file:
    content = file.readline()
    print(content,end="")
    print(f"Apakah file sudah diclose = {file.closed}")

print(f"Apakah file sudah diclose = {file.closed}")