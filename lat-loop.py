#! membuat latihan segitiga 

sisi = 6

#? 1. menggunakan For
print ("awal For")
# dummy variable
count = 1
for i in range(sisi):
    print ("+"*count)
    count += 1

print ("akhir For")


#? 2. mengunakan While
print ("awal While")
count = 1
while True:
    print ("+"*count)
    count += 1
    if count > sisi:
        break

print ("akhir While")


#? 3. ganjil saja (pakai continue)
print ("awal While continue")
count = 1
while True:
    if count % 2:
    #* print jika ganjil
        print ("+"*count)
        count += 1
    else: 
    #* balik keatas lagi jika ganjil
        count += 1
        continue
    
    #* break jika count melebihi sisi
    if count > sisi:
        break

print ("akhir While continue")


#? 4. membuat segitiga sama kaki
print ("awal segitiga")
count = 1
spasi = int(sisi/2)
print (spasi)
while True:
    if count % 2:
    #* print jika ganjil
        print (" "*spasi,"+"*count)
        spasi -= 1
        count += 1
    else: 
    #* balik keatas lagi jika ganjil
        count += 1
        continue
    
    #* break jika count melebihi sisi
    if count > sisi:
        break

print ("akhir segitiga")