n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão: 
      [ 1 ] converter para BINÁRIO
      [ 2 ] converter para OCTAL
      [ 3 ] converter para HEXADECIMAL''')
op = int(input('Sua escolha: '))
if op == 1:
    print('O número {} em binário se torna {}'.format(n, bin(n)[2:]))
elif op == 2:
    print('O número {} em octal se torna {}'.format(n, oct(n)[2:]))
elif op == 3:
    print('O número {} em hexadecimal se torna {}'.format(n, hex(n)[2:]))
else:
    print('Você não digitou uma opção válida!')