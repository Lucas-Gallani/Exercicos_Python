# Calcular a Hipotenusa

from math import sqrt

c1 = float(input('Digite o comprimento do primeiro cateto: '))
c2 = float(input('Digite o compirmento do segundo cateto: '))

calc1 = c1 ** 2
calc2 = c2 ** 2

h = calc1 + calc2

print(f'A hipotenusa será de {sqrt(h):.2f}')



