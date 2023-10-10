n = float(input('Qual é o salário do funcionário? R$'))
d = n + n*15/100
print('O funcionário que ganhava R${:.2f}, com 15% de aumento passa a ganhar R${:.2f}'.format(n, d))