import tools


def main():

    tamanho = int(input('Tamanho do vetor: '))

    vetorA = tools.cria_vetor(tamanho)
    vetorB = tools.cria_vetor(tamanho)
    vetorC = vetorA + vetorB
    print(vetorC)


main()
