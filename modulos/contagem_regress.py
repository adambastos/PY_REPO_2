import time

def contagem(segundos):
    for i in range(segundos, 0, -1):
        print(i)
        time.sleep(1)
    print('Tempo esgotado')

contagem(10)