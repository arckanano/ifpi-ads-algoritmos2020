# Criar vetor
def cria_vetor(tamanho):
    vetor = [0] * tamanho
    return vetor


def adiciona_valor(vetor):
    for i in range(len(vetor)):
        vetor[i] = int(input(f'Insira um valor inteiro na posição {i}: '))
    return vetor


def inverte_vetor(vetor, vetorVazio):
    novo_vetor = vetorVazio
    pos = 0
    for i in range(len(vetor)-1, -1, -1):
        novo_vetor[pos] = vetor[i]
        pos += 1
    return novo_vetor


def verifica_repetido(vetor):
    total_rep = 0
    for i in range(len(vetor)):
        for j in range(i+1, len(vetor)):
            if vetor[i] == vetor[j]:
                total_rep += 1

    return total_rep


# def inter(vetorA, vetorB, vazio):
def inter(vetorC, vazio):
    novo_vetor = vazio
    for i in range(len(vetorC)):
        if i >= len(vetorC)-1:
            break
        elif vetorC[i] == vetorC[i+1]:
            novo_vetor[i] == vetorC[i]

    return novo_vetor


def binToDec(vetor):
    soma = 0
    n = 0
    for i in range(len(vetor)-1, -1, -1):
        p = 2 ** n
        r = p * vetor[i]
        soma += r
        n += 1
    return soma


def binToHex(vet):
    r = ''
    h = [10, 'A', 11, 'B', 12, 'C', 13, 'D', 14, 'E', 15, 'F']
    vet1 = []
    for i in range(len(vet)):
        vet1.append(vet[i])
        if len(vet1) % 4 == 0:
            d = binToDec(vet1)
            if d > 9:
                for i in range(len(h)):
                    if h[i] == d:
                        r += h[i+1]
            else:
                r += str(d)
            vet1.clear()

    return r
