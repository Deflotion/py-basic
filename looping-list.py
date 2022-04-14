
#! looping dari list

#? for loop 
print("\nFor loop")
angka_1 = [1,2,3,4,5,6]

for i in angka_1:
    print(f"angka = {i}")

print("\nNama orang")
orang_1 = ["junet","nuru","taka","oakwokawkoa"]

for o in orang_1:
    print(f"nama = {o}")


#? for loop and range
print("\nFor loop dan range")
angka_2 = [2,4,1,5,2,7]

panjang  = len(angka_2)

for p in range(panjang):
    print(f"angka = {angka_2[p]}")


#? while
print("\nWhile loop")
angka_3 = [2,4,1,5,2,7,8]

panjang  = len(angka_3)
i = 0

while i < panjang:
    print(f"angka = {angka_3[i]}")
    i += 1


#? list comprehension
print("\nList comprehension")
data = ["dedeng",2,4,1,"oren",5,2,7,8]

[print(f"data = {i}") for i in data]

print("\nData kuadrat")
angka = [2,4,1,5,2,7,8]
angka_kuadrat = [i**2 for i in angka]
print(f"angka = {angka_kuadrat}")


#? enumerate
print("\nEnumerate")
data_list = ["dedeng",2,4,1,"oren",5,2,7,8]

for index,data in enumerate(data_list):
    print(f"index = {index}, data = {data}")