# Estruturas condicionais servem para "orientar" o caminho que o código deve seguir

"""
Imagine que você quer começar a treinar calistenia hoje, e para isso,
você precisa saber em qual nível começar de acordo com sua força, 
você deve realizar o máximo de repetições na barra fixa para definir seu nível!
"""

# Primeiro, devemos verificar se o usuário tem uma barra fixa
have_a_pull_up_bar = input("você tem uma barra fixa?(sim/não)").strip().lower()
# .strip() remove espaços extras no início/fim
# .lower() evita problemas com letras maiúsculas/minúsculas

# if significa se, então, se o usuário tiver, entraremos nesse bloco de código
if have_a_pull_up_bar == "sim":
                    # \/ uso de casting para transformar str em int
    pull_ups_reps = int(input("digite a quantidade máxima de repetições na barra fixa: "))
    
    # ifs aninhados (nested ifs): ifs dentro de ifs
    if pull_ups_reps >= 10: 
        print("Nível avançado: vamos aprender muscle-ups!")
    elif pull_ups_reps >= 5: 
        print("Nível intermediário: foco em aumentar a quantidade de repetições!")
    elif pull_ups_reps >= 1: 
        print("Nível iniciante: foco em técnica e resistência")
    else:  
        print("Nível básico: começamos com australian pull ups!")
else:
    print("Sem problemas, vamos começar com exercícios como australian pull-ups usando uma mesa ou barra baixa.")
 
# ⚠️ Obs.: Certifique-se de abranger todos os cenários!

# Match-case, é uma versão do switch case que pode ser encontrado em outras linguagens
# Nos permite definir o valor de uma variável seguindo um conjunto de padrões
# ⚠️ Obs.: disponível a partir do Python 3.10)

day = input("Que dia é hoje? ").strip().lower()

match day:
    case 'segunda':
        print('Dia de treinar costas e bíceps!')    
    case 'terça':
        print('Treino de peito e bíceps!')
    case 'quarta':
        print('Dia de treinar pernas!')
    case 'quinta':
        print('Dia de treinar ombros!')
    case 'sexta':
        print('Dia de treinar core e antebraços!')
    case 'sábado' | 'domingo':
        print('Dia daquele descanso merecido!')
    case _:
        print('Dia inválido. Tente novamente.')

# 🔗 Referências:
# https://www.geeksforgeeks.org/conditional-statements-in-python/
