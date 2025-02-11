produtos = ['TV', 'CELULAR', 'TABLET', 'MOUSE', 'TECLADO', 'GELADEIRA', 'FORNO']
estoque = [100, 150, 100, 120, 70, 90, 80]

baixo_estoque = []

for i, estok in enumerate(estoque):
    if estok < 100:
        baixo_estoque.append(produtos[i])

print(baixo_estoque)

