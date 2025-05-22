# Strings

"""
Strings são sequências de caracteres, Python trata tudo dentro de aspas como uma string.
isso inclui letras, números e símbolos. Python não possuí tipo caracter, então
um caracter único seria uma string de comprimento 1.
"""
# Criando uma String
                    # podem ser criadas usando:
string1 = 'teste um' # aspas simples ou
string2 = "teste dois" # aspas duplas

print(string1, string2)

multi_line_string = """Veja isso é uma 
String com várias 
Linhas! =)"""

print(multi_line_string)

# Acessando os caracteres em uma string
# Caracteres das strings, podem ser acessados usando seu índice,
# esse por sua vez começa em 0

print(string1[0]) # -> t

# Também podemos começar do final
print(string1[-1]) # -> m

# ⚠️ Tentar acessar um índice fora do intervalo vai resultar em IndexError
# só inteiros podem ser usados para acessar o índices, caso use float 
# ou outros tipos vai resultar em TypeError

# Slice String("fatia" de string)
name = 'Lopes'
# (name[inicio:parada:passo]) parada é exclusivo(ex: parada 5 não incluí o índice 5)
print(name[2:5]) # -> pes
# Omitir o primeiro número faz com que comece do ínicio
print(name[:2]) # -> Lo
# Omitir o segundo número faz com que percorra até o fim
print(name[1:]) # -> opes
# Invertendo uma string (no caso cada "passo" é -1)
print(name[::-1]) # - > sepoL 

# Imutabilidade de String
# Strings em python são imutáveis, elas não podem ser mudadas após criadas,
# é necessário usar métodos como concatenação, "fatiamento" ou formatação 
# para manipular strings e criar novas strings com base nas originais

first_name = 'pedro'
# first_name[0] = 'P' -> TypeError
# Se tentar mudar a primeira letra vai obter um erro
print(first_name)

# Então, cria-se uma nova string
first_name = "P" + first_name[1:]
print(first_name)

# Deletando uma string
# Em python não é possível deletar caracteres individuais de uma string, pois
# strings são imutáveis, de qualquer maneira pode-se deletar a string inteira.

del first_name
# ⚠️ Tentar acessar uma string deletada vai resultar em NameError
# afinal essa variável não existe mais

# Atualizando(updating) uma string
# Para atualizar uma string precisa-se criar uma nova string, pois 
# as strings são imutáveis.

name = name + ' Henrique'
print(name) 

name = name.replace('Lopes', 'Pedro')
# ^ cria uma nova string substituindo Lopes por Pedro
print(name)

# Métodos comuns de string 
# Python tem vários métodos nativos para manipular strings, abaixo estão alguns:

print(len(name)) # -> 14 
# retorna o número total de caracteres em uma string

print(name.upper()) # PEDRO HENRIQUE
print(name.lower()) # pedro henrique
# upper converte em uppercase e lower converte em lowercase

name = '**Pedro**'
print(name)

print(name.strip('*'))
# remove espaços(default argument) ou então outros caracteres do ínicio e fim de uma string

print(name.replace('Pedro', '*****'))
# Troca Pedro por *****

# Concatenando e Repetindo strings
# Pode-se repetir-se strings usando * ou concatena-las usando o operador +
print('A gente já chegou? '* 3)
print('A gente vai chegar ' + 'quando chegar!')

# Formatando strings
# Usando o f-string(o jeito mais simples e preferido de formatar)
format_string = ['f-string', 'format()']

print(f'Esse é o {format_string[0]}!')

print('Esse é o {}!'.format(format_string[1]))

# Verificando se uma substring está contida em uma string

fruit = 'banana'
female_name = 'ana'

print(female_name in fruit) # -> True
# verdadeiro pois banana contém ana 


# 🔗 Referências:
# https://www.geeksforgeeks.org/loops-in-python/
