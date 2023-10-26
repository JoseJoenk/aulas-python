n = int(input('Ano de nascimento: '))
i = 2023-n
print('O atleta tem {} anos.'.format(i))
if i <= 9:
    print('Classificado como MIRIM')
elif i <= 14:
    print('Classificado como INFANTIL')
elif i <= 19:
    print('Classificado como JUNIOR')
elif i <= 25:
    print('Classificado como SÊNIOR')
else:
    print('Classificado como MASTER')