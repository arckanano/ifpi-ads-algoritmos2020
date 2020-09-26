import tools


def main():

    tamanho = int(input('Tamanho do vetor: '))
    vetor_A = tools.cria_vetor(tamanho)  # Vetor criado
    valores = tools.adiciona_valor(vetor_A)  # inserir valores

    vetor_vazio = tools.cria_vetor(tamanho)  # Vetor vazio
    vetor_invertido = tools.inverte_vetor(vetor_A, vetor_vazio)
    print(vetor_invertido)


main()
