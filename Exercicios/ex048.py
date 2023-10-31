n = 0
s = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        n = n + 1
        s = s + c
print('A soma de todos os {} números no intervalo é de {}.'.format(n, s))