import tools


def main():

    n = int(input('Quantidade de elementos: '))
    novo_vetor = tools.cria_vetor(n)
    meu_vetor = tools.adiciona_valor(novo_vetor)
    tools.maior_menor_elemento(meu_vetor)


main()
