# Dicionários(Dicts)
"""
Dicionário é uma estrutura de dados que armazena o valor em pares de {chave:valor}
os valores podem ser de qualquer tipo de dados e podem ser duplicados,
já as chaves não podem se repetir e devem ser imutáveis
"""

# Criando dicionários

# usando { }
dict1 = {1: 'Pedro', 2: 'Henrique', 3: 'Lopes'}
print(dict1) # -> {1: 'Pedro', 2: 'Henrique', 3: 'Lopes'}

# usando o construtor dict() 
dict2 = dict(a = 'Pedro', b = 'Henrique', c = 'Lopes')
print(dict2) # -> {'a': 'Pedro', 'b': 'Henrique', 'c': 'Lopes'}

""" ⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️
- da versão 3.7 em diante, os dicionários são ordenados
- as chaves dos dicionários são case sensitive
- chaves devem ser imutáveis; podem ser strings, números ou tuplas, mas NÃO podem ser listas
- chaves devem ser únicas; qualquer chave duplicada substituirá o valor anterior
- o dicionário usa hash; logo pesquisa, inserção, exclusão podem ser executadas em tempo constante
"""

# Acessando itens de um dicionário

# usando chave
print(dict1[1]) # -> Pedro

# usando get()
print(dict2.get('c')) # -> Lopes

# Adicionando e Atualizando itens de um dicionário

# adicionando um novo par chave:valor
dict1[4] = 'Tuca'

# atualizando um valor existente
dict1[1] = 'Peter'

print(dict1) # -> {1: 'Peter', 2: 'Henrique', 3: 'Lopes', 4: 'Tuca'}

# Removendo itens de um dicionário
# pode-se remover itens de um dicionário usando os seguintes métodos

# usando o del para remover um item
del dict1[4]

# usando pop para remover um item e retornar o valor 
value = dict1.pop(3)
print(value) # -> Lopes

# usando popitem para remover e retornar o último par chave:valor
key, value = dict1.popitem()
print(f'Key:{key}, Value: {value}') # -> Key:2, Value: Henrique

# limpando todos os itens de um dicionário
print(dict2) # -> {'a': 'Pedro', 'b': 'Henrique', 'c': 'Lopes'} 
dict2.clear()
print(dict2) # -> {}

# Iterando através de um dicionário

# iterando sobre as chaves
for key in dict1:
    print(key) # -> 1

# iterando sobre os valores
for value in dict1.values():
    print(value) # -> Peter

# iterando sobre os pares chave:valor
for key, value in dict1.items():
    print(f'{key}:{value}') # -> 1:Peter

# dicionários aninhados(nested Dictonary)
# quando dicionários contém outros dicionários
dict3 = {1: 'My life is ', 2:'Code:',
         3: {'A': 'Calisthenics,', 'B': 'Outdoors,', 'C': 'Datasci', 'D': '& Experiences'}}
print(dict3)

# 🔗 Referências:
# https://www.geeksforgeeks.org/python-dictionary/