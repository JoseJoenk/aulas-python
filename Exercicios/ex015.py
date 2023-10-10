d = int(input('Por quantos dias o carro foi alugado? '))
km = int(input('Quantos quilometros ele rodou? '))
dd = d * 60
kmd = km * 0.15
print('O valor total a pagar é de R${:.2f}'.format(dd + kmd))