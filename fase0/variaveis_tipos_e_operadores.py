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

"""
Assim como diferentes tipos de calçados, temos diferentes tipos de variáveis.
"""

# Como descobrir o tipo de uma variável?
print(type(age))  # <class 'int'>

# Principais tipos em Python:

# Tipos Numéricos
inteiro = 10         # int
decimal = 3.14       # float
complexo = 2 + 3j    # complex

# tipos sequenciais
string = 'strings'  # <class 'str'> — pode usar aspas simples ou duplas

lista = ['calistenia', 'gatos', 'natureza', 'pão de queijo', 27]  # <class 'list'>
# uma lista de coisas que eu gosto + meu número da sorte (sim, pão de queijo é essencial)

tupla = (1998, 'Itajubá')  # <class 'tuple'>
# parecida com lista, mas imutável — meus gostos mudam, minha cidade e ano de nascimento não

# Tipo Booleano
blue_eyes = False # Meus olhos não são azuis
brown_eyes = True # Meus olhos são castanhos

# Tipo Conjunto (Set)
numbers_of_lottery = {23, 56, 12, 4, 30, 7, 27}  # <class 'set'> — sem ordem, mutáveis, sem duplicatas

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
# Relacionais: ==, !=, >, <, >=, <=
# Lógicos: and, or, not
# Atribuição: =, +=, -=, *=, /=, etc.

