def add(prod, qnt) -> None:
    print('-- Adicionar produto --')
    prod = input('Nome do produto: ')
    qnt = int(input('Quantidade: '))
    produtos[prod] = qnt

def remove(prod, qnt) -> None:
    print('-- Remover produto --')
    prod = input('Nome do produto: ')
    qnt  = int(input('Quantidade'))
    new_qnt = 0
    if qnt > qnt:
        print('Você não possui toda essa quantidade em estoque.')
    else
    del produtos[prod]

def show_list() -> None:
    print('Lista atualizada: ')
    print(produtos)


produtos = {}
prod = ''
qnt = 0
opt = ''
print('Escolha uma opção: ')

while opt != 4:
    opt = int(input(' 1 - Inserir produto \n 2 - Remover produto \n 3 - Ver lista \n 4 - Sair \n'))
    if opt == 1:
        add(prod, qnt)
    elif opt == 2:
        remove(prod, qnt)
    elif opt == 3:
        show_list()
    elif opt == 4:
        print('Programa encerrado.')
        break

    
