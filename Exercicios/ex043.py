peso = float(input('Qual é seu peso? Kg '))
altura = float(input('Qual é sua altura> m '))
imc = peso / altura**2
print('Seu imc é {:.2f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso normal.')
elif imc < 25:
    print('Você está no peso ideial.')
elif imc < 30:
    print('Você está em sobrepeso.')
elif imc < 40:
    print('Você está com obesidade.')
else:
    print('Obesidade morbida.')
