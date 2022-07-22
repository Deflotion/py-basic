import datetime

#! multikeys
mahasiswa1 = {
    'nama':'ujang',
    'nim':'1021093',
    'sks_lulus':130,
    'beasiswa':False,
    'lahir':datetime.datetime(2001,3,21) #? urutan (thn,bln,hari)
}

mahasiswa2 = {
    'nama':'ujin',
    'nim':'1024093',
    'sks_lulus':144,
    'beasiswa':True,
    'lahir':datetime.datetime(2000,4,21) #? urutan (thn,bln,hari)
}

mahasiswa3 = {
    'nama':'ujo',
    'nim':'1021043',
    'sks_lulus':144,
    'beasiswa':True,
    'lahir':datetime.datetime(2000,6,22) #? urutan (thn,bln,hari)
}

#! dictionary didalam dictionary
data_mahasiswa = {
    'Mah001':mahasiswa1,
    'Mah002':mahasiswa2,
    'Mah003':mahasiswa3,
}

print(f"{'Key':<7} {'Nama':<10} {'SKS':<3} {'beasiswa':<9} {'Lahir':<10}")
print("-"*50)
for mahasiswa in data_mahasiswa:
    KEY = mahasiswa
    NAMA = data_mahasiswa[KEY]['nama']
    NIM = data_mahasiswa[KEY]['nim']
    SKS = data_mahasiswa[KEY]['sks_lulus']
    BEASISWA = data_mahasiswa[KEY]['beasiswa']
    LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")
    
    print(f"{KEY:<7} {NAMA:<10} {SKS:<3} {BEASISWA:^9} {LAHIR:<10}")