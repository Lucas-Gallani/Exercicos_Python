# Conversão de Celsius em Fahrenheit

celsius = float(input('Digite a temperatura em ºC'))
f = celsius * 1.8 + 32
print(f'{celsius}ºC convertido em Fahrenheit são {f}ºF')

fahrenheit = float(input('Digite a temperatura em ºF'))
c = fahrenheit - 32 * 1.8
print(f'{fahrenheit}ºC convertido em Fahrenheit são {c:.2f}ºF')