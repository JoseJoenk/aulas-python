import random
pc = random.randint(1, 5)
n = int(input('Vou pensar em um número entre 1 e 5. Em que número eu pensei?' ))
if pc == n:
    print('Você acertou! Eu pensei em {} mesmo.'.format(pc))
else:
    print('Você errou. Eu pensei no número {} e não em {}'.format(pc, n))
