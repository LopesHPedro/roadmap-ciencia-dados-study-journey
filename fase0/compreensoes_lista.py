# Compreensões de lista(List compreheensions)
"""
A compreensão de lista é uma maneira mais elegante e eficiente de criar lista em Python,
condensando um laço de repetição em uma única linha.
"""
numbers = [1,2,3,4,5]

squares = [number ** 2 for number in numbers]

print(squares) # -> [1, 4, 9, 16, 25] 
"""
 Sintaxe 

 [expressão for item in iterável if condição]

 expressão: a transformação ou valor a ser íncluido na nova lista
 item: o elemento atual retirado do iterável
 iterável: uma sequência ou coleção(ex: listas, tuplas, sets)
 if condição(opcional): uma condição decide se o item deve ser incluído

 Essa sintaxe permite combinar iteração, modificação e filtragem na mesma linha
 """

# For loop vs. list compreheension
# o for loop requer várias linhas já a list compreheension apenas uma
# exemplo, descobrindo os pares
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = []

for number in numbers:
    if number % 2 == 0:
        even.append(number)
print(even) # -> [2, 4, 6, 8, 10]

even.clear()
print(even) # -> []

even = [number for number in numbers if number % 2 == 0]
print(even) # -> [2, 4, 6, 8, 10]

# Examplos:

# criando uma lista a partir do range
list1 = [number for number in range(10)]
print(list1) # -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# usando loops aninhados(nested) para gerar uma lista de pares de coordenadas(x, y)
coordinates = [(x,y) for x in range(3) for y in range(3)]
print(coordinates) # -> [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

# unindo listas
mat = [[1, 2, 3], 
       [4, 5, 6],
       [7, 8, 9],
]

one_line = [value for row in mat for value in row]

print(one_line) # -> [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 🔗 Referências:
# https://www.geeksforgeeks.org/python-list-comprehension/