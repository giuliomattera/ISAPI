lista = ['farina', 10, True]

for element in range(len(lista)):
    print(lista[element])

del element

for element in lista:
    print(element)
    
import MyLibrary as nik

pippo = nik.my_first_function(5, 10)
nik.altro()