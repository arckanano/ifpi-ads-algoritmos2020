# criar matriz quadrada
from random import randint, randrange


def n_random():
    # return randint(1, 100)
    return randrange(100)


def criar_matriz_quadrada(ordem):
    vetor = [[0]*ordem]*ordem
    return vetor

v = criar_matriz_quadrada(3)

for i in range(len(v)):
    for j in range(len(v[i])):
        print(f'Linha {i} >>> Elemento {j}')
        v[i][j] = int(input('Dado: '))


print(v)
