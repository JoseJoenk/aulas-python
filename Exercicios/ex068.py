from random import randint
e = 'e'
c = 0
while True:
    n = int(input('Diga um valor: '))
    while e not in 'P' and e not in 'I':
        e = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    pc = randint(1, 10)
    s = n + pc
    if s%2 == 0:
        print(f'Você jogou {n} e o computador {pc}. Total de {s} DEU PAR!')
        if e == 'P':
            print('Você Venceu!')
            c += 1
            e = 'e'
        else:
            print('Você Perdeu!')
            break
    else:
        print(f'Você jogou {n} e o computador {pc}. Total de {s} DEU ÍMPAR!')
        if e == 'I':
            print('Você Venceu!')
            c += 1
            e = 'e'
        else:
            print('Você Perdeu!')
            break   
print(f'GAME OVER! Você venceu {c} vezes.')