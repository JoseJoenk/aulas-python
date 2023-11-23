n = 0
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*15)
    c = 1
    if n < 0:
        break
    while c <= 10:
        print(f'{n} x {c} = {n*c}')
        c += 1
print('Programa encerrado.')