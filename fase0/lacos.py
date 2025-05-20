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
