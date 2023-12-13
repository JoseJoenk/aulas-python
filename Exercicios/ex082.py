valores = []
par = []
impar = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] ')).strip()[0]
    if resp in 'Nn':
        break
for c in valores:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)
valores.sort()
par.sort()
impar.sort()
print(f'{valores}')
print(f'{par}')
print(f'{impar}')