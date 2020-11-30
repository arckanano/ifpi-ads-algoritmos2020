import tools


def main():

    tamanho = int(input('Tamanho dos vetores: '))
    vetorA = tools.cria_vetor(tamanho)
    vetorB = tools.cria_vetor(tamanho)

    print('Adicionar dados do vetor A')
    dadosVetorA = tools.adiciona_valor(vetorA)
    print('Adicionar dados do vetor B')
    dadosVetorB = tools.adiciona_valor(vetorB)

    print('CONJUNTO UNIÃO DE A E B')
    vetorC = vetorA + vetorB
    print(vetorC)

    print('INTERSECÇÃO DOS VETORES A E B')
    vetor_vazio = tools.cria_vetor(0)
    # vetorD = tools.inter(vetorA, vetorB, vetor_vazio)
    vetorD = tools.inter(vetorC, vetor_vazio)
    print(vetorD)

main()