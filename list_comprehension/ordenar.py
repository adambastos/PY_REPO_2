precos = [30, 25, 15, 40]
produtos = ['arroz', 'açucar', 'mamao', 'cafe']

list_final = list(zip(precos, produtos))
list_final.sort(reverse=True)
print(list_final)

lista_final = [produto for preco, produto in list_final]

print(lista_final)


