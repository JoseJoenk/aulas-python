loop = True
n1 = int(input('Primeiro Número: '))
n2 = int(input('Segundo Número: '))
while loop == True:
    print('''
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos Números
    [ 5 ] Sair''')
    op = int(input('Qual é a sua opção? '))
    if op == 1:
        print('A soma entre {} + {} é {}'.format(n1, n2, n1+n2))
    elif op == 2:
        print('A multiplicação entre {} x {} é {}'.format(n1, n2, n2*n2))
    elif op == 3:
        if n1 > n2:
            print('Entre {} e {}, o maior é {}'.format(n1, n2, n1))
        elif n2 > n1:
            print('Entre {} e {}, o maior é {}'.format(n1, n2, n2))
        else:
            print('Os dois números são iguais.')
    elif op == 4:
        print('Escolha seus novos números: ')
        n1 = int(input('Primeiro Número: '))
        n2 = int(input('Segundo Número: '))
    elif op == 5:
        loop = False
    else:
        print('Essa não é uma opção válida.')
print('Até um outro dia.')