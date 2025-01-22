def cadastro_prod(nome, valor):
    return print('O produto {} foi cadastrado com o valor de R${}' .format(nome, valor))

nome = input('Nome do produto: ')
valor = float(input('Valor do produto: '))

cadastro_prod(nome, valor)


