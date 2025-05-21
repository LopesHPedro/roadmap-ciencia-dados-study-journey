# Funções

"""
Benefícios das funções 
	- Aumentam a legibilidade do código
	- Aumentam a reusabilidade do código 
"""
# Declarando uma função
# def é uma keyword(palavra reservada)
def name_of_function(parameter):
	# Instruções a serem realizadas
	return # Expressão que pode ser retornada

"""
Existem dois tipos de função:
	- As funções "Built-in", funções padrão do Python que estão disponíveis,
alguns exemplos: print(), input(),int()...
	- As funções criadas pelos desenvolvedores: podemos criar nossas própŕias funções
como veremos a seguir.
"""

# Criando uma função 
    # Nome da função
def print_salutations():
	   print('Seja bem-vindo ao meu código!')
        # Instrução a ser realizada

# Chamando uma função
print_salutations()

# Função com parâmetros
# Uma função pode receber parâmetros
def calcualte_double(number:int):
    # No caso number seria o parâmetro e :int o tipo de dado
    double = number * 2 
    print(double)

# Argumentos, são os valores passados nas funções
calcualte_double(8)
               # ^ No caso 8 seria um argumento

# Tipos de Argumentos: default, keyword, positional & arbitrary

# default argument
# O argumento tem um valor padrão pré-definido
def greetings(name='visitor'):
    print(f'Welcome, {name}!')

greetings() 
# Caso não seja passado argumento ele imprime o valor padrão

# positional argument
# Argumentos passados na ordem exata dos parâmetros
def name_and_age(name, age):
    print(f'Seu nome é {name} e sua idade é {age}')

name_and_age("Lopes", 27) # Aqui a ordem importa

# keyword argument
# O parâmetro é nomeado ao passar o argumento
name_and_age(age=27, name="Lopes") # Aqui a ordem não importa

# arbitrary argument: *args & **kwargs
# *args                             # veremos o que são tuplas futuramente!    
# Permite passar vários positional arguments como tuplas
def total(*numbers):
    print(sum(numbers))

total(1,2,3)

# **kwargs                             # veremos o que são dicionários futuramente!    
# Permite passar vários keywords arguments como dicionários
def show_info(**data):
    for key, value in data.items():
        print(f'{key}: {value}')

show_info(name='Lopes', age=27)

# Docstring
# A primeia string após uma funcão é chamada de Document string
# ou Docstring de maneira abreviada, e ela é usada para descrever
# a funcionalidade da funcão
# ⚠️ seu uso é opcional mas é considerado uma boa prática!

def calisthenics():
    """This function prints 'Calistenia é demais!'"""
    print('Calistenia é demais!')

print(calisthenics.__doc__)

# Function with a Function
# Função internar ou até mesmo Função aninhada, é quando
# uma função tem outra função dentro de si.
def prepare_travel(destination):
    backpack = ['Barraca', "Garrafa d'água", 'frutas', 'protetor solar']
    
    def checklist(): # essa seria a função interna
        print(f'\nVamos para {destination} 🌄')
        print('Você vai precisar dos seguintes items:')
        for item in backpack:
            print(f'- {item}')
    
    checklist() # chamada direta da função interna
    
prepare_travel('Trindade')

# Anonymous Functions (lambda)
# Função sem nome, normalmente usada para coisas simples e rápidas.
half = lambda x: (x/2)
print(half(5))

# Recursive Functions
# São funções que chamam elas mesmas, útil para problemas 
# matemáticos ou recursivos, um bom exemplo de seu uso são fatorias
def factorial(n):
    if n == 0:  
        return 1 # Caso base(condição de parada) evita loop infinito
    else:
        return n * factorial(n - 1) # Caso recursivo, a função se chama novamente

print(factorial(4))

# Return statement
# Serve para retornar um valor da função
def difference(a,b):
    return a - b
    
result = difference(10, 8)
print(result)

# Pass by reference
def change_list(list1):
     list1.append(99) # Muda a lista

my_list = [1, 2, 3]
print()
"""
✅ Mutáveis → Dá pra mudar o conteúdo:

    list → listas

    dict → dicionários

    set → conjuntos

    bytearray
"""

# Pass by value 
def altera_numero(num):
    num = 99  # Só muda a cópia

meu_numero = 1
altera_numero(meu_numero)
print(meu_numero)  # Resultado: 1
"""
❌ Imutáveis → Não dá pra mudar, só criar outro:

    int → inteiros

    float → decimais

    str → strings

    tuple → tuplas

    frozenset → conjuntos congelados

    bool → booleanos

    bytes → sequência de bytes
"""


# 🔗 Referências:
# https://www.geeksforgeeks.org/python-functions/