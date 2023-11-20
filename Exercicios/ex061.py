n = int(input('Primeiro Termo: '))
r = int(input('Razão da PA: '))
c = 0
while c < 10:
    print('{} > '.format(n), end='')
    n = n + r
    c = c + 1
print('Fim')
