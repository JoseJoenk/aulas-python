listanum = []
max = 0
min = 0
for c in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a Posição {c}: ')))
    if c == 0:
        max = min = listanum[c]
    else: 
        if listanum[c] > max:
            max = listanum[c]
        if listanum[c] < min:
            min = listanum[c]
print(f'Você digitou os valores {listanum}')
print(f'O maior valor digitado foi {max} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == max:
        print(f'{i}... ', end='')
print()
print(f'O menor valor digitado foi {min} nas posições ', end='')
for i, v in enumerate(listanum):
    if v == min:
        print(f'{i}... ', end='')
print()