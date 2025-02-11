'''
1. Crie uma lista vazia para armazenar os itens da lista de compras.
2. Crie um loop infinito que imprima um menu de opções ao usuário e permita que ele escolha uma opção.
3. Dentro do loop, use uma declaração if para executar a tarefa apropriada de acordo com a escolha do usuário.
4. Se o usuário escolher adicionar um item, solicite que ele digite o nome do item e adicione-o à lista.
5. Se o usuário escolher remover um item, solicite que ele digite o nome do item e remova-o da lista.
6. Se o usuário escolher ver a lista, mostre cada item da lista em sua própria linha.
7. Se o usuário escolher sair, encerre o loop usando break.

'''
def insere(prod) -> None:
    prod = input('Insira o nome do produto a ser adicionado: ')
    print('')
    lista_compras.append(prod)

def remove(prod) -> None:
    prod = input('Insira o nome do produto a ser removido: ')
    print('')
    if prod in lista_compras:
        lista_compras.remove(prod)
    else:
        print('Este produto não consta na lista.')
    
def show_list():
    print('Lista de compras atualizada: ')
    print('')
    print(lista_compras)


lista_compras = []
opt = 0

while opt != 4:
    prod = ''
    opt = int(input(' 1 - Inserir produto \n 2 - Remover produto \n 3 - Ver lista \n 4 - Sair \n'))
    if opt == 1:
        insere(prod)
    elif opt == 2:
        remove(prod)
    elif opt == 3:
        show_list()
    elif opt == 4:
        print('Programa encerrado.')
        break
    else:
        print('Opção incorreta!')

print(lista_compras)