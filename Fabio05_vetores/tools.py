# Criar vetor
def cria_vetor(tamanho):
    vetor = [0] * tamanho
    return vetor


def adiciona_valor(vetor):
    for i in range(len(vetor)):
        vetor[i] = int(input(f'Insira um valor inteiro na posição {i}: '))
    return vetor


    