n = int(input('Primeiro Termo: '))
r = int(input('Razão da PA: '))
c = 0
t = 1
f = 10
while c < 10:
    print('{} > '.format(n), end='')
    n = n + r
    c = c + 1
print('Parô!')
while t != 0:
    t = int(input('Quantos termos você quer mostrar a mais? '))
    c = 0
    while c < t:
        print('{} > '.format(n), end='')
        n = n + r
        c = c + 1
    f = f + t
    print('Parô!')
print('Progressão finalizada com {} termos mostrados.'.format(f))
