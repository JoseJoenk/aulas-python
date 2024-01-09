from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 20),
        'jogador2': randint(1, 20),
        'jogador3': randint(1, 20),
        'jogador4': randint(1, 20)}
ranking = []
print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'O {k} tirou {v} no D20.')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]} pontos.')
    sleep(1)