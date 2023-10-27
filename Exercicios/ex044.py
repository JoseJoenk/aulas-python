p = float(input('Preço das compras: R$'))
print('''Formas de pagamento
    [ 1 ] à vista dinheiro/cheque
    [ 2 ] à vista no cartão
    [ 3 ] 2x no cartão
    [ 4 ] 3x ou mais no cartão''')
f = int(input('Qual é a opção? '))
if f == 1:
    print('A sua compra que custaria R${:.2f} no final vai custar R${:.2f}'.format(p, p-(p*10/100)))
elif f == 2:
    print('A sua compra que custaria R${:.2f} no final vai custar R${:.2f}'.format(p, p-(p*5/100)))
elif f == 3:
    print('A sua compra vai custar R${:.2f} com duas parcelas de R${:.2f} cada.'.format(p, p/2))
elif f == 4:
    d = int(input('Quantas parcelas? '))
    v = p + (p*20/100)
    print('A sua compra será parcelada em {}x de R${:.2f} com JUROS.\nSua compra de R${:.2f} vai custar R${:.2f} no final.'.format(d, v/d, p, v))
else:
    print('Por favor, escolha uma opção válida.')