import os
import CRUD as CRUD

if __name__ == "__main__":
    sistem_operasi = os.name
    
    match sistem_operasi:
            case "nt": os.system("cls")
    
    print("SELAMAT DATANG DI PROGRAM")
    print("  DATABASE PERPUSTAKAAN  ")
    print("=========================")
    
    #$ check database ada/tidak
    CRUD.init_console()
    
    while(True):
        match sistem_operasi:
            case "nt": os.system("cls")
        print("SELAMAT DATANG DI PROGRAM")
        print("  DATABASE PERPUSTAKAAN  ")
        print("=========================")
        print(f"1. Read data")
        print(f"2. Create data")
        print(f"3. Update data")
        print(f"4. Delete data\n")
        user_option = input("Masukan opsi: ")
        
        match user_option:
            case "1": CRUD.read_console()
            case "2": CRUD.create_console()
            case "3": CRUD.update_console()
            case "4": CRUD.delete_console()
        is_done = input("Apakah selesai (y/n)? ")
        if is_done == 'y' or is_done == 'Y':
            break
    print("Program telah selesai, Terima kasih telah menggunakannya")