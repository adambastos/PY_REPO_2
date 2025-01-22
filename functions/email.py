def filtra(email, provedor):
    for item in email:
        if provedor in item:
            print(item)
    return True
        

emails = [
    "joao123@gmail.com",
    "maria.silva@uol.com",
    "pedro.almeida@hotmail.com",
    "ana_clara@gmail.com",
    "lucas_oliveira@uol.com",
    "carla.souza@hotmail.com",
    "fernando.rocha@gmail.com",
    "juliana.santos@uol.com",
    "ricardo.martins@hotmail.com",
    "camila.lima@gmail.com"
]

lista = filtra(emails, 'gmail')
print(lista)
