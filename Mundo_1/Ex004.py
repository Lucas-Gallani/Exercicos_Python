# Mostrando os tipos primitivos da variável

var = input('Digite algo: ')

print(f'''
O tipo primitivo deste valor é {type(var)}
Só tem espaços? {var.isspace()}
É um número? {var.isnumeric()}
É alphanúmerica? {var.isalnum()}
Está em maiuscula? {var.isupper()}
Está em minuscula {var.islower()}
Está capitalizada? {var.istitle()}
''')