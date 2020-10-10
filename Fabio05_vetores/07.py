import tools


def main():
    n = int(input('Quantidade de elementos: '))
    novo_vetor = tools.cria_vetor(n)
    meu_vetor = tools.adiciona_valor(novo_vetor)

    b = []
    for i in range(len(meu_vetor)):
        if meu_vetor[i] % 2 == 0:
            b.append(0)
        else:
            b.append(1)
    print(b)


main()
