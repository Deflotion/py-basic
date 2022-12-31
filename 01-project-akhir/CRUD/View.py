from . import Operasi

def read_console():
    data_file = Operasi.read()
    
    index = "No"
    judul = "Judul"
    penulis = "Penulis"
    tahun = "Tahun"

    #$ Header
    print("\n"+"="*100)
    print(f"{index:4} | {judul:40} | {penulis:40} | {tahun:5}")
    print("-"*100)
    
    #$ Data
    for index,data in enumerate(data_file):
        data_break = data.split(",")
        pk = data_break[0]
        date_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4]
        print(f"{index+1:4} | {judul:.40} | {penulis:.40} | {tahun:4}",end="")

    #$ Footer
    print("="*100+"\n")

def create_console():
    print("\n\n"+"="*100)
    print("Silahkan tambah data buku")
    print("="*100+"\n")
    penulis = input("Penulis\t: ")
    judul = input("Judul\t: ")
    while(True):
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("Maks 4 doang bwanggg mana ada tahun lebih dari 4")
        except:
            print("\nTahun harus angka bwaaang!!!")
    
    Operasi.create(tahun,judul,penulis)
    print("\nberimkut Damta bamru amda gann")
    read_console()
    print("="*100)

def update_console():
    read_console()
    while(True):
        no_buku = int(input("Pimlih bumku yang imngin diumbah gannn: "))
        data_buku = Operasi.read(index=no_buku)
        data_break = data_buku.split(',')
        pk = data_break[0]
        data_add = data_break[1]
        penulis = data_break[2]
        judul = data_break[3]
        tahun = data_break[4][:-1]
        if data_buku:
            break
        else:
            print("Nomor timdak vamlid gannnn")
    
    
    
    while(True):
        #? form data yg ingin di update
        print("\n"+"="*100)
        print("Simlahkan pimlih bamgian mamna yang imngin diumbah: ")
        print(f"1. judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:4}")
        
        #? memilih mode utk update
        user_option = input("Pimlih gan: ")
        print("\n"+"="*100)
        match user_option:
            case "1" : judul = input("Judul\t: ")
            case "2" : penulis = input("Penulis\t: ")
            case "3" : 
                while(True):
                    try:
                        tahun = int(input("Tahun\t: "))
                        if len(str(tahun)) == 4:
                            break
                        else:
                            print("Maks 4 doang bwanggg mana ada tahun lebih dari 4")
                    except:
                        print("\nTahun harus angka bwaaang!!!")
            case _: print("Imdexnya gada bwanggg!!!")
        
        print("Damta bamru anda")
        print(f"1. judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:4}")
        
        is_done = input("Apakah selesai update(y/n)? ")
        if is_done == 'y' or is_done == 'Y':
            break
        
    Operasi.update(no_buku,pk,data_add,tahun,judul,penulis)

def delete_console():
    read_console()
    while(True):
        no_buku = int(input("Pimlih bumku yang imngin didemlete gannn: "))
        data_buku = Operasi.read(index=no_buku)
        
        if data_buku:
            data_break = data_buku.split(',')
            pk = data_break[0]
            data_add = data_break[1]
            penulis = data_break[2]
            judul = data_break[3]
            tahun = data_break[4][:-1]

            #? form data yg ingin di delete
            print("\n"+"="*100)
            print("Damta yang imngin dihampus: ")
            print(f"1. judul\t: {judul:.40}")
            print(f"2. Penulis\t: {penulis:.40}")
            print(f"3. Tahun\t: {tahun:4}")
            
            is_done = input("Mau hampus(y/n)? ")
            if is_done == 'y' or is_done == 'Y':
                Operasi.delete(no_buku)
                break
        else:
            print("Nomor timdak vamlid gannnn")
    print("Damta temlah dihampus")