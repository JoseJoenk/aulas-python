c = int(input('Qual é o valor da casa? '))
s = float(input('Qual é o salário do comprador? '))
p = int(input('Em quantos anos ele quer pagar? '))
m = c / (p*12)
t = s * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}'.format(c, p, m))
if m <= t:
    print('Empréstimo pode ser CONCEDIDO')
else:
    print('Empréstimo NEGADO')