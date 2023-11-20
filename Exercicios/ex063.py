t = int(input('Quantos termos você quer mostrar? '))
c = 0
n0 = 0
n1 = 1
n2 = 0
while c < t:
    print('{} > '.format(n1), end='')
    n2 = n1
    n1 = n1 + n0
    n0 = n2
    c = c + 1
print('GG')