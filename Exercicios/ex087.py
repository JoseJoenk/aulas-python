matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
s = max = col = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor: [{l}, {c}] '))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            s += matriz[l][c]
    print()
print(f'A soma dos valores pares é: {s}')
for l in range(0, 3):
    col += matriz[l][2]
print(f'A soma dos valores da terceira coluna é {col}')
for c in range(0, 3):
    if c == 0:
        max = matriz[1][c]
    else:
        if matriz[1][c] > max:
            max = matriz[1][c]
print(f'O maior número da linha dois é {max}')