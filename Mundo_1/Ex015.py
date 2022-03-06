# Aluguel de Carro

dias = int(input('Dias alugado: ')) 
km = float(input('Quilômetros rodados: '))

perdia = 60.0 * dias
perkm = 0.15 * km
total = perdia + perkm

print(f'O total a pagar pelo aluguel do carro será de R${total:.2f}')


