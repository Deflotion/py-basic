## Teknik menduplikat list

a = ["momon","turu","coeg"]
print (f"a = {a}")

b = a #! pass by reference
print (f"b = {b}")

#? merubah member dari a
#! ini akan merubah kedua list
a[1] = "jordan"
b.sort()
print (f"a = {a}")
print (f"b = {b}")

#! keluarkan address dari kedua list a dan b
print (f"address a = {hex(id(a))}")
print (f"address b = {hex(id(b))}")

#? menduplikat list dengan menggunak copy
print ("Menampilkan list c dengan a.copy()")
c = a.copy()#! full duplicate / new data
print (f"address a = {hex(id(a))}")
print (f"address b = {hex(id(b))}")
print (f"address c = {hex(id(c))}")

print (f"a = {a}")
print (f"b = {b}")
print (f"c = {c}")

print ("Merubah data c ke-0")
c[2] = "mimin"
print (f"a = {a}")
print (f"b = {b}")
print (f"c = {c}")

print ("Merubah data a ke-1")
a[1] = "jor"
print (f"a = {a}")
print (f"b = {b}")
print (f"c = {c}")
