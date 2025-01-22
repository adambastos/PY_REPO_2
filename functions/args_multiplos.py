#Ou seja, se você quiser pegar o valor associado à chave 'soma', por exemplo, deve acessar opcoes['soma'].

#Ordem correta dos argumentos
def exemplo(arg, *args, kwargs= 10, **argumentos):
    return 0

def operacoes(valor, **opcoes):
    result = 0
    if 'soma' in opcoes:
        result += valor + opcoes['soma']
    if 'multi' in opcoes:
        result += valor * opcoes['multi']
    if 'subt' in opcoes:
        result += valor - opcoes['subt']
    if 'div' in opcoes: 
        result += valor / opcoes['div']
    return result

print(operacoes(10, soma=10))
print(operacoes(10, multi=10))
print(operacoes(10, subt=10))
print(operacoes(10, div=10))