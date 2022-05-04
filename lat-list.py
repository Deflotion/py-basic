
#! program list buku

list_buku = []
while True:
    print("\nMasukan data buku")
    judul = input("Judul Buku\t:")
    penulis = input("Nama Penulis\t:")

    data_buku = [judul,penulis]
    list_buku.append(data_buku)
    
    print("\n\nNo. | Judul | Penulis")
    for index,buku in enumerate(list_buku):
        print(f"{index+1} | {buku[0]} | {buku[1]}")
    print("="*20)
    lanjut = input("Mau lanjut?(y/n)")
    
    if lanjut == "n":
        break

print("Selesai")