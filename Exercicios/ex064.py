n = 0
c = 0
t = 0
while n != 999:
    n = int(input('Digite um número [999 para parar]: '))
    t = t + n
    c = c + 1
print('Você digitou {} números e a soma entre eles foi {}.'.format(c-1, t-999))