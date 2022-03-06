# Randomizar lista de alunos

from random import shuffle

a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 =  str(input('Quarto aluno: '))

lista = [a1.capitalize(), a2.capitalize(), a3.capitalize(), a4.capitalize()]

shuffle(lista)

print(f'A ordem dos alunos será {lista}')