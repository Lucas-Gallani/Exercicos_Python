# Calcular desconto de um produto

preco = float(input('Digite o preço do produto R$'))
desc = preco - preco * 0.05
print(f'O produto que custava R${preco}, com o desconto de 5% vai passar a custar R${desc:.2f}')

