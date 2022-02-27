# Calculo de média

nome = str(input('Digite o nome do aluno: ')).strip().title()
n1 = int(input('Primeira nota: '))
n2 = int(input('Segunda nota: '))
m = (n1 + n2) / 2

print(f'A média do(a) aluno(a) {nome} foi de {m}')