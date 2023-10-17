from math import hypot
n1 = float(input('Quanto mede o cateto oposto? '))
n2 = float(input('Quanto mede o cateto adjacente? '))
h = hypot(n1, n2)
print('A hipotenusa mede {}'.format(h))