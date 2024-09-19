from operator import truediv
from pickle import LIST


lista = list([" hola", " buenas", 23,45,67, True ])

cantidad_de_elemtos = len(lista)

lista.insert(2, " toma")
print(cantidad_de_elemtos)
print(lista)

lista.pop(2)

print(lista)

print(len(lista))

lista.sort()

print(lista)
