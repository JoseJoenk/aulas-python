from random import randint
pc = randint(1, 10)
c = 0
print(pc)
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
pj = int(input('Qual é o seu palpite? '))
while pj != pc:
    if pc > pj:
        pj = int(input('Mais... faça outra tentativa. '))
        c += 1
    elif pc < pj:
        pj = int(input('Menos... faça outra tentativa. '))
        c += 1
print('Ahá, você acertou. Meu número pensado era {} e você acertou em {} tentativas.'.format(pc, c))