# Conjuntos

"""
Um conjunto em Python é uma coleção não ordenada de vários itens com tipos diferentes
são mutáveis, não indexados e não contém duplicatas, a ordem pode mudar.
"""

# Criando conjuntos
# usando {} é o jeito mais eficiente e básico de se criar um conjunto 
set1 = {1,2,3} # -> {1, 2, 3}
print(set1)

# usando a função set() 
set2 = set() 
print(set2) # -> set()

# criando conjuntos usando uma lista, uma tupla e um dicionário
# útil para quando for necessário remover duplicatas
set_list = set(['Lopes', 'Pedro', 'Lopes'])
print(set_list) # -> {'Lopes', 'Pedro'}
set_tuple = set(('Lopes', 'Pedro', 'Lopes'))
print(set_tuple) # -> {'Lopes', 'Pedro'}
set_dict = set({'Lopes': 1, 'Pedro': 2, 'Lopes':3})
print(set_dict) # -> {'Lopes', 'Pedro'}

"""⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️ 
- Um conjunto só pode conter imutáveis(int, float, str, tuple(a tuple só deve ter imutáveis))
- A ordem dos elementos não é necessariamente a mesma da ordem que foram adicionados
- Itens duplicados serão removidos
- Não suportam indexação, se tentar vai resultar em TypeError
"""

# Adicionando elementos 
print(set1) # -> {1, 2, 3}

# adicionando um item
set1.add(8)

# adicionando múltiplos itens
set1.update([5,6])

print(set1) # -> {1, 2, 3, 5, 6, 8} 
# como pode-se ver a ordem não é mantida

# Acessando conjuntos
print(set1)

# acessando elementos usando loop for
print('Os elementos são:', end=' ')
for element in set1:
    print(element, end=' ') # -> {1, 2, 3, 5, 6, 8}
print()

# conferindo se um elemento está no conjunto usando o in
print(3 in set1) # -> True # 3 está no conjunto

# Removendo elementos
# Pode-se usar vários métodos para remover elementos de um conjunto:

print(set1) # -> {1, 2, 3, 5, 6, 8}

# usando remove()
set1.remove(3)
print(set1) # -> {1, 2, 5, 6, 8}
# set1.remove(25)
# ⚠️ ao tentar remover um valor não presente vai resultar em KeyError

# usando discard()
set1.discard(8)
print(set1) # -> {1, 2, 5, 6}
set1.discard(35)
# ⚠️ aqui ao tentar remover um valor não presente NÃO vai resultar erro

# usando pop()
value = set1.pop() # -> retira um valor e manda para value
print(value) 
# ⚠️ como o set é não ordenado não podemos garantir qual valor vai sair

# usando clear()
print(set1) # -> {2, 5, 6}
set1.clear()
print(set1) # -> set()
#set1.pop()
# ⚠️ tentar usar pop() em um set vazio resulta em KeyError

# Frozen-sets
# Muito parecido com os sets mas com a difereça que são imutáveis, uma vez criados
# não se pode modificar elementos ou seja não é possível adicionar, remover ou mudar 
# qualquer item, assim como sets frozen-sets não podem conter itens duplicados

# Criando um frozenset

# a partir de uma lista
fset = frozenset([1, 2, 3, 4, 5])
print(fset) # -> frozenset({1, 2, 3, 4, 5})

# a partir de um set
fset = frozenset({5, 4, 2, 3, 1})
print(fset) # -> frozenset({1, 2, 3, 4, 5})

# 🔗 Referências:
# https://www.geeksforgeeks.org/python-sets/