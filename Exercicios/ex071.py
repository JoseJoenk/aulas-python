cont50 = cont20 = cont10 = cont1 = 0
valor = int(input('Que valor você quer sacar? R$'))
if valor >= 50:
    while valor >= 50:
        valor -= 50
        cont50 += 1
if valor >= 20:
    while valor >= 20:
        valor -= 20
        cont20 += 1
if valor >= 10:
    while valor >= 10:
        valor -= 10
        cont10 += 1
if valor >= 1:
    while valor >= 1:
        valor -= 1
        cont1 += 1
if cont50 > 0:
    print(f'Total de {cont50} cédulas de R$50')
if cont20 > 0:
    print(f'Total de {cont20} cédulas de R$20')
if cont10 > 0:
    print(f'Total de {cont10} cédulas de R$10')
if cont1 > 0:
    print(f'Total de {cont1} cédulas de R$1')
print('Programa encerrado família, sextou.')