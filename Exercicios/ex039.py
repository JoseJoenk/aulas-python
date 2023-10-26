n = int(input('Ano de nascimento: '))
n3 = 2023-n
print('Quem nasceu em {} terá {} anos em 2023.'.format(n, n3))
if n3 < 18:
    print('Ainda faltam {} anos para o alistamento\nSeu alistamento será em {}'.format(18-n3, n+18))
elif n3 > 18:
    print('Você já deveria ter se alistado a {} anos.\nSeu alistamento foi em {}'.format(n3-18, n+18))
else:
    print('Você tem que se alistar IMEDIATAMENTE!')