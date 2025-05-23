# Listas
""" 
Usamos para guardar itens de todos os tipos(incluindo outra lista). Algumas informações sobre listas:
- Uma lista pode ser mista(conter itens de diferentes tipos)
- A lista é mutável, podemos modificar ou substituir os itens
- A lista é ordenada sempre seguindo a ordem dos elementos com base em como eles são adicionados
- O acesso pode ser feito diretamente usando a posição do índices(começa a partir do zero)
"""

# ⚠️ A lista armazena referências não valores
# A lista armazena referências(ponteiros) que indicam
# onde cada objeto está armazenado na memória.

# Criando listas
list1 = [27, 'cachoeira', 3.14, True] # usadno colchetes
list2 = list((1,2,3, 'batata', 4,5)) # usando o list() constructor
list3 = [0] * 5 # criando uma lista com elementos repetidos

# Acessando os elementos de uma lista
print(list1[0]) # -> 27 
print(list2[3]) # -> batata
print(list3[2]) # -> 0
print(list1[3]) # -> True

# Adicionando os elementos em uma lista
# Pode-se adicionar elementos em uma lista usando os seguintes métodos:

list4 = ['frutas'] 

list4.append('suco de uva') 
# adiciona no final da lista
print(list4) # -> ['frutas', 'suco de uva']

list4.insert(0,'batata frita') 
# adiciona no índice especificado (0 neste caso)
print(list4) # -> ['batata frita', 'frutas', 'suco de uva']

list4.extend(['água com gás', 'limão', 'lasanha'])
# adiciona múltiplos elementos no final da lista
print(list4) # -> ['batata frita', 'frutas', 'suco de uva', 'água com gás', 'limão', 'lasanha']

# Atualizando os elementos em uma lista
# Pode-se mudar o valor de um elemento acessando-o usando seu índice
list5 = [1,9,3,4,5,6] 
print(list5) # -> [1, 9, 3, 4, 5, 6]
list5[1] = 2
print(list5) # -> [1, 2, 3, 4, 5, 6]

# Removendo os elementos de uma lista
# Pode-se remover elementos de uma lista usando:

list5.remove(6) # remove a primeira ocorrência de valor 6 no caso
print(list5) # -> [1, 2, 3, 4, 5]

my_number = list5.pop(1) # remove o elemento do índice 1 (2)
print(list5) # -> [1, 3, 4, 5]
print(my_number)

del list5[2] # deleta o elemento de índice 2 (4)
print(list5) # -> [1, 3, 5]

# Iterando sobre listas
# Pode-se facilmente iterar sobre uma lista usando um loop for ou outros métodos
# de iteração, é útil quando queremos fazer uma operação em cada item
# ou até mesmo acessar valores específicos com base em certas condições:

# Usando um loop for:
print('\nminha lista de compra:')
for item in list4:
    print(item)
print()

# Listas aninhadas(Nested-Lists)
# Uma lista aninhada é uma lista que contém outra lista, é útil para representar matrizes ou tabelas
# pode-se acessar listas aninhadas encadeando os índices

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print(matrix[2][0]) #-> 7

# 🔗 Referências:
# https://www.geeksforgeeks.org/python-lists/