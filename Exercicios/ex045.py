from random import randint
print('''Suas opções:
      [ 1 ] Pedra
      [ 2 ] Papel
      [ 3 ] Tesoura''')
j1 = int(input('Qual é a sua jogada? '))
if 0 < j1 > 3:
    print('Por favor, digite uma opção válida.')
else:
    if j1 == 1:
        e1 = 'Pedra'
    elif j1 == 2:
        e1 = 'Papel'
    else:
        e1 = 'Tesoura'
    j2 = randint(1, 3)
    if j2 == 1:
        e2 = 'Pedra'
    elif j2 == 2:
        e2 = 'Papel'
    else:
        e2 = 'Tesoura'
    if j1 == 1 and j2 == 2 or j1 == 2 and j2 == 3 or j1 == 3 and j2 == 1:
        print('Eu escolhi {} e você {}, eu VENCI!'.format(e2, e1))
    elif j2 == 1 and j1 == 2 or j2 == 2 and j1 == 3 or j2 == 3 and j1 == 1:
        print('Eu escolhi {} e você {}, VOCÊ venceu.'.format(e2, e1))
    else:
        print('Nós dois escolhemos {}, é um empate.'.format(e1))