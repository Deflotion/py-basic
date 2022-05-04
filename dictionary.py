 #todo list -> array, mengakses dengan menggunakan index

#? menggunakan index
data_list = ['ucup','momon','tatang']
print(data_list[0])

#? dictionary (dict) -> associative array
#* cara mengakses associative array menggunakan 
#* indentifier -> key
#* menggunakan kurung {}
#* akan berguna jika menggunakan data 
#* yang punya struktur

data_dict = {
    'key':'value',
    'cp':'ucup',
    'mn':'momon',
    'ang':'tatang',
    'nmbr':1000,
    'list':data_list,
}

print(data_dict['ang'])
print(data_dict['nmbr'])
print(data_dict['list'])