n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
m = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f} a média do aluno é {:.1f}'.format(n1, n2, m))
if m < 5:
    print('Aluno REPROVADO!')
elif m >= 5 and m < 7:
    print('Aluno em RECUPERAÇÃO')
else:
    print('Aluno APROVADO!')