"""
Pense em variáveis como caixas onde você pode armazenar valores.

Regras para nomear variáveis:
- Devem conter apenas caracteres alfanuméricos e underscores (_)
- Devem começar com uma letra ou underscore
- São **case-sensitive** (ex: nome, Nome e NOME são diferentes)
- Não podem usar palavras reservadas do Python
- Bons nomes tornam o código mais legível (boa prática, não regra)
"""

# Como criar uma variável?
name_of_variable = "Lopes"  # strings usam aspas simples ou duplas

number = 27                 # números inteiros ou decimais sem aspas
age = lucky_number = 27     # múltiplas variáveis com o mesmo valor

# Liberando espaço de memória:
del number

# Permitindo que o usuário insira dados
write_a_sentence = input("Digite seu texto aqui: ")
# ⚠️ Toda entrada pelo input é do tipo string (str), mesmo que digite um número

"""
Assim como diferentes tipos de calçados, temos diferentes tipos de variáveis.
"""

# Como descobrir o tipo de uma variável?
print(type(write_a_sentence))  # <class 'str'>
# ^ Provando que toda entrada é uma String

# Principais tipos em Python:

# Tipos Numéricos
inteiro = 10         # int
decimal = 3.14       # float
complexo = 2 + 3j    # complex

# Tipos sequenciais
string = 'strings'  # <class 'str'> — pode usar aspas simples ou duplas

lista = ['calistenia', 'gatos', 'natureza', 'pão de queijo', 27]  # <class 'list'>
# Uma lista de coisas que eu gosto + meu número da sorte (sim, pão de queijo é essencial)

tupla = (1998, 'Itajubá')  # <class 'tuple'>
# Parecida com lista, mas imutável — meus gostos mudam, minha cidade e ano de nascimento não

# Tipo Booleano
blue_eyes = False # Meus olhos não são azuis
brown_eyes = True # Meus olhos são castanhos

# Tipo Conjunto (Set)
lottery_numbers = {23, 56, 12, 4, 30, 7, 27}  # <class 'set'> — sem ordem, mutáveis, sem duplicatas

# Tipo Dicionário
dicionario = {
    'altura': 1.84,
    'idade': 27
}  # dict — chave: valor

# Type Casting (conversões)
idade_str = str(age)       # int → str
peso_float = float("84.0") # str → float
numero_int = int(3.99)     # float → int (trunca, não arredonda)

# Operadores em Python
# Aritméticos: +, -, *, /, //, %, **
# Usamos para realizar operações matemáticas
total = (1 + 1 - 1) * 1 / 1 # Aqui temos as operações básicas (soma, subtração, multiplicação e divisão)
rounded_division = 5//2 # Divisão inteira (descarta as casas decimais) > 2
rest_of_division = 5 % 2 # Resto de divisão > 1
exponentiation = 3 ** 2 # 3 elevado a 2 > 9

# Relacionais: ==, !=, >, <, >=, <=
# Usamos para comparar dois valores, se atenderem ao critério retorna True, senão retorna False
# == compara se dois valores são iguais, != compara se dois valores são diferentes
print('lopes' == 'lopes', 5 != 5) # True False
# > compara se um valor é maior que outro, < compara se um valor é menor que outro
print(2 > 5, 4 < 100) # False True
# >= compara se um valor é maior ou igual a outro, <= compara se um valor é maior ou igual a outro
print(3 >= 3, 80 >= 10) # True True

# Lógicos: and, or, not
# and(e) quando uma coisa e outra precisam ser verdades
age = 27 # Eu tenho 27 E(and)
voterID = True # Eu tenho título de eleitor
can_vote = age >= 18 and voterID # No caso ambas são verdadeiras 
print(can_vote) # Logo eu posso votar (True)

# or(ou) quando é necessário apenas uma coisa ser verdade
its_hot = False # Embora NÃO esteja quente
calisthenics_train_today = True # Eu treinei calistenia
im_thirsty = calisthenics_train_today or its_hot # No caso apenas um é verdadeiro 
print(im_thirsty) # Então estou com sede (True)

# not(não) é a negação de algo(o oposto)
print(not(calisthenics_train_today)) # False

# Atribuição: =, +=, -=, *=, /=, etc.
contador = 10 # Atribui um valor ao contador
contador += 5  # Agora contador vale 15
contador *= 2  # Agora contador vale 30
contador /= 15 # Agora contador vale 2
contador -= 2 # Subtrai 2 de 2 > contador vale 0

# 🔗 Referências:
# https://www.geeksforgeeks.org/introduction-to-python/
# https://www.geeksforgeeks.org/python-variables/
# https://www.geeksforgeeks.org/python-operators/
# https://www.geeksforgeeks.org/python-data-types/
