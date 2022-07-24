'''Type Hints pada function'''
import string

#! bentuk standar function
#* studi kasus
# def fungsi(parameter):
#     hasil = parameter**2
#     return hasil

# fungsi(1)
# fungsi("Ucup")
# fungsi(True)

#$ penggunaan type hints
def sepuluh_pangkat(argument:int) -> int:
    pangkat = argument**2
    return pangkat

total = sepuluh_pangkat(5)
print(total)

def display(argument:string):
    print(argument)

display("ucok")

