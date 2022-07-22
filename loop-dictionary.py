 #! looping dictionary


nama_orang = {
    "pe":"momon",
    "pi":"ray",
    "zr":"azrel",
    "sp":"asep",
    "zs":"zafier"
}

#* looping first try (outputnya adalah key)
for orang in nama_orang:
    print(orang)

#* operator mengambil item/iterables
#$ mengambil key
keys = nama_orang.keys()
print(keys)

for key in nama_orang.keys():
    print(nama_orang.get(key))


#$ mengambil value
values = nama_orang.values()
print(values)

for value in nama_orang.values():
    print(value)


#$ mengambil item
items = nama_orang.items()
print(items)

for item in nama_orang.items():
    print(item)

for key,value in nama_orang.items():
    print(f"Key = {key}, Value = {value}")