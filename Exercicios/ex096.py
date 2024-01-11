def area(l, c):
    a = l * c
    print(f'A área de um terreno com {l}x{c} é de {a}m².')

l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
area(l, c)