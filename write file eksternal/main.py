
#! tutorial write file eksternal

#$ 1. mode write 
#$ dia akan membuat file baru jika tidak ada 
#$ lalu akan menimpa atau overwrite isinya

with open("write file eksternal/data_1.txt",'w',encoding="utf-8") as file:
    file.write("ucok acok")
with open("write file eksternal/data_1.txt","w",encoding="utf-8") as file:
    file.write("awikwok")
with open("write file eksternal/data_1.txt","w",encoding="utf-8") as file:
    file.write("overwrite")

#$ 2. mode append
with open("write file eksternal/data_2.txt","w",encoding="utf-8") as file:
    file.write("acok cok\n")
with open("write file eksternal/data_2.txt","a",encoding="utf-8") as file:
    file.write("acoeg sekali\n")
with open("write file eksternal/data_2.txt","a",encoding="utf-8") as file:
    file.write("akan bertambah terus")

#$ 3. mode r+
with open("write file eksternal/data_3.txt",'w',encoding="utf-8") as file:
    file.write("data ke-3\n")
with open("write file eksternal/data_3.txt","r+",encoding="utf-8") as file:
    file.write("baris-1\n")
    file.write("baris-2\n")
    file.write("baris-3\n")

with open("write file eksternal/data_3.txt","r+",encoding="utf-8") as file:
    data = file.read()
    print(data)

with open("write file eksternal/data_3.txt","r+",encoding="utf-8") as file:
    file.write("awikwok banget") #? menimpa isi text sesuai panjang data
