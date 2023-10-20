n = float(input('Qual é o salário do funcionário? R$'))
if n < 1250:
    n = n + n*15/100
    print('Seu salário recebeu um aumento de 15%! A partir de agora, seu salário é de R${}'.format(n))
else:
    n = n + n*10/100
    print('Seu salário recebeu um aumento de 10%! A partir de agora, seu salário é de R${}'.format(n))