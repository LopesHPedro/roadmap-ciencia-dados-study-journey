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

# Laços (ou loops) são usados no código quando você precisa repetir uma ação
""" 
Imagine que um mineiro tenha um pote cheio de pães de queijo,
Ele abre o pote, pega um pão de queijo e come. E faz isso de novo, e de novo...
Imagine ter de escrever isso manualmente.
Por sorte podemos usar um loop, enquanto houver pães de queijo, ele continua comendo!
"""
# while
brazilian_cheese_bread = 10

while(brazilian_cheese_bread >= 1):
    brazilian_cheese_bread -= 1
    if brazilian_cheese_bread > 0:
        print("O mineiro comeu um pão de queijo, ainda restam", brazilian_cheese_bread)
else:
    print("O mineiro comeu o último pão de queijo\nLá se foram os pães de queijo! =(\n")
"""
⚠️ Deve-se tomar cuidado para não criar um loop infinito
se ao invés de subtrair fosse somada um pão de queijo
o programa rodaria infinitamente!!
"""
    
""" 
Imagine um aficionado por natureza, que tenha um quintal grande,
Enquanto houver espaço ele planta uma árvore. E faz isso de novo, e de novo...
Mas seu quintal tem um limite, há espaço para no máximo 6 árvores.
Vamos plantar árvores? 
"""
# for
for tree in range(1, 7):
    print(f"Uma árvore foi plantada, no quintal há {tree} árvore(s) plantada(s)")
    # f"string {variavel}" - f-strings incluem variáveis dentro de strings de forma prática
else:
    print("O quintal está lindo e lotado, não cabem mais árvores!\n")

# Nested Loops(Laços aninhados)
""" 
Imagine que você quer se desafiar ao máximo em um treino de calistenia
e para isso você decide criar um desafio de circuito variando exercícios
e o numero de repetiçoes
"""
exercises = ['Muscle-ups', 'Handstand push-ups', "L-sits", "Pistol Squats"]

for reps in range(1, 6):
    for move in exercises:
        print(f"Faça {reps} {move}.")
    if reps < 5:
        print(f"descanse {reps} minuto(s).\n")
    else: 
        print("Parabéns você concluiu o treinamento!\n")

# Loop Control Statments
"""
Vamos supor que você quer atingir uma meta específica de flexões 
primeiro você define a meta e depois faz uma,
caso consiga fazer uma flexão você faz a próxima 
caso não consiga você para.
"""
push_ups = 1
goals = int(input("Digite a sua meta: "))

print('Vamos lá! faça uma flexão')
for i in range(2, (goals + 1)):
    keep_going = input('Você consegue continuar? (sim/nao)\n')
    if keep_going == 'sim':
        push_ups += 1
        print(f"você fez {push_ups} flexões!")
        continue # Continue statement
    elif keep_going == 'nao':
        print(f"você fez {push_ups} flexões, descanse e tente mais tarde!")
        break # Break statement
    else:
        print('Entrada inválida, digite apenas sim ou nao')
        pass # Pass statement
        
if push_ups == goals:
    print('Parabéns, você atingiu sua meta!')

# 🔗 Referências:
# https://www.geeksforgeeks.org/loops-in-python/
