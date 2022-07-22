 #* copy dictionary

orang = {
    "pe":"momon",
    "pi":"ray",
    "zr":"azrel",
    "sp":"asep",
    "zs":"zafier"
}

human = orang.copy()

print(f"orang : {orang}\n")
print(f"human : {human}\n")

orang["pe"] = "punten"
print(f"orang : {orang}\n")
print(f"human : {human}\n")


#* pop dictionary (mengambil data berdasarkan key)
dataAsep = human.pop("sp")
print(f"dataAsep: {dataAsep}\n")
print(f"human: {human}\n")

#* popitem dictionary (hanya mengambil data paling terakhir)
dataAkhir = human.popitem()
print(f"dataAkhir: {dataAkhir}\n")
print(f"human: {human}\n")

#cat tambahan: dictionary sangat berguna jika kita mempunyai
#cat strucktur yang jelas dari si dictionarynya