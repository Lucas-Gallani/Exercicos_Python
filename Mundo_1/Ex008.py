# Conversão de medidas de distância

metros = float(input('Distância em metros: '))

km = metros / 1000  # Quilômetro
hm = metros / 100  # Hectrômetro
dam = metros / 10  # Decametro
dm = metros * 10  # Decimetro
cm = metros * 100  # Centímetro
mm = metros * 1000  # Milímetro

print(f'Convertendo {metros} metros....\nQuilômetros: {km}km\nhectrômetros: {hm}hm\nDecametros: {dam}dam\nDecimetros: {dm}dm\nCentimetros: {cm}cm\nMilimetros {mm}mm')


