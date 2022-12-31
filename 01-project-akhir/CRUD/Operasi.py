import os
from . import Database
from .Util import random_string
import time

def create_first_data():
    penulis = input("Penulis: ")
    judul = input("Judul: ")
    while(True):
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("Maks 4 doang bwanggg mana ada tahun lebih dari 4")
        except:
            print("\nTahun harus angka bwaaang!!!")
    
    data = Database.TEMPLATE.copy()
    
    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H:%M:%Sz",time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)
    
    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'
    print(data_str)
    
    try:
        with open(Database.DB_NAME,'w',encoding='utf8') as file:
            file.write(data_str)
    except:
        print("Gamgal imput bwang!")

def create(tahun,judul,penulis):
    data = Database.TEMPLATE.copy()
    
    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H:%M:%Sz",time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)
    
    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'
    
    try:
        with open(Database.DB_NAME,'a',encoding='utf8') as file:
            file.write(data_str)
    except:
        print("Gamgal nammbah damta bwang!")

def read(**kwargs):
    try:
        with open(Database.DB_NAME,'r') as file:
            content = file.readlines()
            jumlah_buku = len(content)
            if "index" in kwargs:
                index_buku = kwargs["index"]-1
                if index_buku > jumlah_buku or index_buku < 0:
                    print("Bumku timdak amda bwangggg!!")
                    return False
                else:      
                    return content[index_buku]
            else:
                return content
    except:
        print("Data tidak ada bwang!")
        return False

def update(no_buku,pk,data_add,tahun,judul,penulis):
    data = Database.TEMPLATE.copy()

    data["pk"] = pk
    data["date_add"] = data_add
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)

    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'
    
    panjang_data = len(data_str)

    try:
        with(open(Database.DB_NAME,'r+',encoding="utf-8")) as file:
            file.seek(panjang_data*(no_buku-1))
            file.write(data_str)
    except:
        print("emrror damlam update damta")

def delete(no_buku):
    print(Database.DB_NAME)
    try:
        with open(Database.DB_NAME,'r') as file:
            counter = 0
            while(True):
                content = file.readline()
                if len(content) == 0:
                    break
                elif counter == no_buku - 1:
                    pass
                else:
                    with open("data_temp.txt",'a',encoding="utf-8") as temp_file:
                        temp_file.write(content)
                counter+=1 
    except:
        print("Database error")
    
    os.replace("data_temp.txt",Database.DB_NAME) 
    
    