def filtra(lista, provedor):
    lista_filtrada = []
    for item in lista:
        if provedor in item:
            lista_filtrada.append(item)
    return lista_filtrada


emails = [
    "joao.silva@gmail.com",
    "maria.oliveira@hotmail.com",
    "pedro.santos@uol.com",
    "ana.pereira@gmail.com",
    "lucas.ferreira@hotmail.com",
    "carla.rodrigues@uol.com",
    "juliana.martins@gmail.com",
    "fernando.gomes@hotmail.com",
    "beatriz.moura@uol.com",
    "roberto.souza@gmail.com"
]

lista = filtra(emails, 'gmail.com')
print('\n' .join(map(str, lista)))  
