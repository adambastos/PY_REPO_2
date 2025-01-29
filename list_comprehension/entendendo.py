precos = [30, 25, 15, 40]
produtos = ['arroz', 'açucar', 'mamao', 'cafe']

impostos = []
for item in precos:
    impostos.append(item * 0.3)

print(impostos)

impostos_list = [item * 0.3 for item in precos]
print(impostos_list)

def calcula_imposto(preco, imposto):
    return preco * imposto
imposto_func = [calcula_imposto(preco, 0.3) for preco in precos]
print(imposto_func)