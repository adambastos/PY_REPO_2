'''
1 - Peça ao usuário para inserir uma lista de números separados por espaço.
2 - Conte quantas vezes cada número aparece na lista.
3 - Exiba o resultado na forma de um dicionário, onde a chave é o número e o valor é a quantidade de vezes que ele aparece.

'''

dicio = {}
nums = list(map(int, input('Digite a sequência de números: ').split()))
for i, y in enumerate(nums):
    dicio[y] = y
print(dicio)

