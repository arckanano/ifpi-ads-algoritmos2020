import tools


def main():

    tamanho = int(input('Tamanho do vetor: '))
    vetor_A = tools.cria_vetor(tamanho) # Vetor criado
    valores = tools.adiciona_valor(vetor_A)

    vetor_B = tools.cria_vetor(tamanho)

    for i in range(len(valores)-1, -1, -1):
        print(vetor_B[i], valores[i])
        vetor_B[i] = valores[i]
    print('vetor b', vetor_B)


main()
