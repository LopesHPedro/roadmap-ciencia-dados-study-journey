# Tuplas

"""
Uma tupla em Python é uma coleção ordenada e imutável de elementos(que podem ser de tipos diferentes), 
são similiares a listas, entretando após sua criação não podem ser modificadas
"""

# Criando tuplas 
# uma tupla vazia
tuple1 = ()
print(tuple1) # -> ()

# usando strings
tuple1 = ('Amarelo', 'Azul')
print(tuple1) # -> ('Amarelo', 'Azul')

# usando listas
tuple1 = ([1,2,3],[4,5,6])
print(tuple1) # -> ([1, 2, 3], [4, 5, 6])

# usando a função interna do python
tuple2 = tuple('Lopes')
print(tuple1) # -> ('L', 'o', 'p', 'e', 's')

# ainda é possível criar tuplas de tuplas
tuple3 = (tuple1,tuple2) 
print(tuple3) # -> (([1, 2, 3], [4, 5, 6]), ('L', 'o', 'p', 'e', 's'))

# Acessando tuplas
# Pode-se acessar os elementos de uma tupla usando indexação e fatiamento(slicing)
# similar a maneira como se faz com uma lista

# acessando com o índice
tuple1 = tuple('Pedro')
print(tuple1[0]) # -> P

# acessando um intervalo de elementos usando o fatiamento(slicing)
print(tuple1[1:4]) # -> ('e', 'd', 'r')
print(tuple1[:3]) # -> ('P', 'e', 'd')

# 'descompactando' um tupla(Tuple unpacking)
tuple2 = ('rio', 'mar', 'lago') # -> ('rio', 'mar', 'lago')
print(tuple2)

# essa linha vai descompactar os valores da tupla2
a,b,c = tuple2
print(a) # -> rio
print(b) # -> mar
print(c) # -> lago

# Concatenação de tuplas
# Pode-se concatenar uma tupla usando o operador +
# ⚠️ Só se pode combinar os mesmos tipos de dados com concatenação 
# se você tentar combinar uma tupla com lista vai resultar em TypeError

print(tuple3) # -> (([1, 2, 3], [4, 5, 6]), ('L', 'o', 'p', 'e', 's'))
tuple3 = tuple1 + tuple2
print(tuple3) # -> ('P', 'e', 'd', 'r', 'o', 'rio', 'mar', 'lago')

# Fatiamento(slicing) de uma tupla
# Pode-se criar uma nova tupla com elementos de outra tupla

tuple4 = tuple('DataScientist')

# removendo o primeiro elemento
new_tuple = tuple4[1:]
print(new_tuple) # -> ('a', 't', 'a', 'S', 'c', 'i', 'e', 'n', 't', 'i', 's', 't')

# invertendo a tupla
new_tuple = tuple4[::-1]
print(new_tuple) # -> ('t', 's', 'i', 't', 'n', 'e', 'i', 'c', 'S', 'a', 't', 'a', 'D')

# imprimindo os elementos do intervalo
new_tuple = tuple4[4:7]
print(new_tuple) # -> ('S', 'c', 'i')

# Deletando uma tupla
# Pode-se deletar uma tupla inteira, mas como tuplas são imutáveis 
# não é possível deletar seus elementos individualmente

del tuple1

# print(tuple1) -> NameError (pois a variável não está definida) :)


# 🔗 Referências:
# https://www.geeksforgeeks.org/python-tuples/