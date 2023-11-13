n = int(input('Digite um número para calcular seu fatorial: '))
c = n
print('Calculando {}! = {} '.format(n, c), end='')
while c > 1:
    c = c - 1
    print('x {} '.format(c), end='')
    n = n * c
print('= {}'.format(n))