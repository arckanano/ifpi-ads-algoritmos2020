from random import randrange, randint

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


def maior_menor_elemento(meu_vetor):
    menor = meu_vetor[0]
    pos_menor = 0
    maior = meu_vetor[0]
    pos_maior = 0
    for i in range(len(meu_vetor)):
        if meu_vetor[i] > maior:
            maior = meu_vetor[i]
            pos_maior = i
        elif meu_vetor[i] < menor:
            menor = meu_vetor[i]
            pos_menor = i

    return menor, maior


def ordem_crescente(vetor):
    for i in range(len(vetor)-1):
        j = i+1
        if vetor[i] > vetor[j]:
            temp = vetor[i]
            vetor[i] = vetor[j]
            vetor[j] = temp
            ordem_crescente(vetor)


def cria_matriz_quadrada_aleatoria(ordem):
    # Cria um novo vetor com outros vetores dentro
    m_quadrada = []
    for i in range(ordem):
        m_quadrada.append(cria_vetor(ordem))

    # preenche o vetor criado com números aleatórios
    for i in range(len(m_quadrada)):
        for j in range(len(m_quadrada[i])):
            m_quadrada[i][j] = randrange(10)
    
    return m_quadrada