 #? operator dictionary

data_dict = {
    "pe":"pepsi",
    "da":"date",
    "du":"adudu"
}

#* panjang dictionary
lendict = len(data_dict)
print(f"Panjangnya adalah: {lendict}")

#* mengecek key exist atau tidak
KEY = "pe"
checkkey = KEY in data_dict
print(f"Apakah {KEY} ada di data_dict = {checkkey}")

#* mengakses value (read) dengan get
print(data_dict["pe"])
print(data_dict.get("pe"))
print(data_dict.get("pee","data tidak ditemukan")) #$ cek key dengan message tidak ditemukan

#* mengupdate data 
data_dict["pe"] = "aqua"
print(data_dict)

#* menambah data 
data_dict["pes"] = "vit"
print(data_dict)

#* cara mudahnya
data_dict.update({"pe":"pepsi"})
print(data_dict)
data_dict.update({"pee":"pepsiii"}) #$ kalau data tidak ada otomatis menambah
print(data_dict)

#* mendelete data pada dictionary
del data_dict["pee"]
print(data_dict)
