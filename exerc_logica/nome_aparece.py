'''
Peça ao usuário para inserir uma frase.
Conte quantas vezes cada palavra aparece na frase (ignorando maiúsculas/minúsculas).
Exiba as palavras e suas frequências em formato de dicionário.

'''
dicio = {}
frase = list(map(str, input('Digite a frase: ').split()))
cont = 0
for word in frase:
    if word in dicio:
        dicio[word] += 1
    else:
        dicio[word] = 1
print(dicio)