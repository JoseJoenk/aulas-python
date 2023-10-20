v = int(input('Qual é a velocidade atual do carro? '))
if v > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h \nVocê deve pagar uma multa de RS{:.2f}'.format((v-80)*7))
print('Tenha um bom dia! Dirija com segurança!')