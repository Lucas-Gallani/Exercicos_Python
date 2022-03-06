# Calcular a quantia de litros de tinta

l = float(input('Digite a largura da parede: '))
a = float(input('Digite a altura da parede: '))
area = l * a
tinta = area / 2

print(f'Com uma área de {area}m², Você precisaria de {tinta} litros de tinta')