# Calcular Seno, Cosseno, Tangente

from math import sin, cos, tan, radians

angulo = int(input('Digite o angulo a ser calculado: '))

s = sin(radians(angulo))
c = cos(radians(angulo))
t = tan(radians(angulo))

print(f'''
Calculando o angulo de {angulo}
O seu seno é de {s:.2f}
O seu cosseno é de {c:.2f}
E sua  tangente é de {t:.2f}
''')