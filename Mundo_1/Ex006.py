# Dobro, Triplo e Raiz de um número

from math import sqrt

n = int(input('Digite um número: '))

dobro = n * 2
triplo = n * 3
raiz = sqrt(n)

print(f'Analisando o número {n}...\nO seu dobro é {dobro}\nO seu triplo é {triplo}\nE a sua raiz quadrada é {raiz:.2f}')