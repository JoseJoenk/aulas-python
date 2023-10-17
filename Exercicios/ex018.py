from math import sin
from math import cos
from math import tan
from math import radians
a = float(input('Digite o ângulo que você deseja: '))
n = radians(a)
print('O ângulo de {} tem: \nO SENO de {}\nO COSENNO de {}\nA TANGENTE de {}'.format(a, sin(n), cos(n), tan(n)))