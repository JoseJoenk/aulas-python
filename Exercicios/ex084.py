temp = []
princ = []
max = min = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        max = min = temp[1]
    else:
        if temp[1] > max:
            max = temp[1]
        if temp[1] < min:
            min = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] ')).strip()[0]
    if resp in 'Nn':
        break
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
print(f'O maior peso foi de {max}kg. Peso de: ', end='')
for p in princ:
    if p[1] == max:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi de {min}kg. Peso de: ', end='')
for p in princ:
    if p[1] == min:
        print(f'[{p[0]}] ', end='')