n = str(input('Digite seu nome: ')).strip()
n = n.split()
print('Muito prazer em te conhecer!\n Seu primeiro nome é {}\nSeu último nome é {}'.format(n[0], n[len(n)-1]))