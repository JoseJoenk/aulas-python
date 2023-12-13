num = []
while True:
    n = int(input('Digite um valor: '))
    if n not in num:
        num.append(n)
        print('Número adicionado com sucesso.')
    else: 
        print('Esse número já existe.')
    r = str(input('Quer continuar? [S/N] ')).strip()[0]
    if r in 'Nn':
        break
num.sort()
print(f'Você digitou os valores {num}')