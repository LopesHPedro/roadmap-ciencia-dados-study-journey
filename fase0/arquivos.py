# Arquivos(.csv, .txt)

"""
Em Python ler arquivos é essencial para importar e analisar dados
.txt arquivo de texto puro, armazena qualquer sequência de caracteres
.csv(Comma-Separated Values) são valores separados por vírgulas:
 - padrão universal para a troca de dados
 - cada linha representa um registro; cada coluna, um campo.
 - pode ser separado por vírgulas, ponto e vírgula, ou tabulação
"""

# Para arquivos .txt

# Abrir arquivos: open()

file =  open('filename', 'mode')

"""
Principais modos:
'r' -> leitura (padrão)
'w' -> escrita (sobrecreve)
'a' -> append (adiciona ao final)
'b' -> modo binário
'+' -> leitura e escrita
"""

# exemplo
file = open('data.txt', 'r')

# Ler arquivos
file.read() # -> lê tudo como string
file.readline() # -> lê uma linha
file.readlines() # -> lê uma lista de linhas

# Escrever
file.write('texto') # -> escreve uma string
file.writelines(lista) # -> escreve uma lista de strings

# Fechar arquivos
file.close()

# gerenciamento automático
with open('data.txt', 'r') as file:
    data = file.read()

"""
Modos Combinados
    'rb', 'wb' -> arquivos binários
    'r+' -> leitura e escrita
    'w+' -> sobrescreve e lê
    'a+' -> adiciona e lê
"""

# Exemplo csv 
import csv

# Lendo csv
with open('data.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

# Escrita com csv
with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['nome', 'idade', 'cidade'])
    writer.writerow(['Pedro', 27, 'Itajubá'])

# Leitura baseada em dicionários(mais prático quando o CSV tem cabeçalho)
with open('data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['nome'], row['idade'])

# Escrita baseada em dicionários(mais prático quando o CSV tem cabeçalho)
with open('output.csv', 'w', newline='') as csvfile:
    fieldnames = ['nome', 'idade']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'nome': 'Pedro', 'idade': 27})

# Tratamento de exceções ao abrir arquivos
try:
    with open('data.txt', 'r') as file:
        data = file.read()
except FileNotFoundError: 
    print("Arquivo não encontrado.")
except IOError:
    print("Erro ao ler o arquivo.")

"""⚠️⚠️⚠️⚠️⚠️⚠️⚠️⚠️
O bloco try permite que você teste um trecho de código que pode gerar um erro. 
Se ocorrer um erro dentro do bloco try, o Python interrompe a execução desse bloco 
e passa para o bloco except, onde você pode lidar com o erro de forma controlada.
"""


# https://www.geeksforgeeks.org/file-handling-python/
# https://www.geeksforgeeks.org/reading-and-writing-csv-files-in-python/