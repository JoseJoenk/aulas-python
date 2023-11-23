n = c = t = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    c += 1
    t += n
print(f'A soma dos {c} valores é {t}!')