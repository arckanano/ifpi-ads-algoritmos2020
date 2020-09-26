import tools


def main():

    tamanho = int(input('Tamanho do vetor: '))
    vetorA = tools.cria_vetor(tamanho)
    dados = tools.adiciona_valor(vetorA)

    contador = tools.verifica_repetido(dados)
    if contador > 0:
        print('Há elementos repetidos no vetor!')
    else:
        print('Não há elementos repetidos no vetor!')


main()
