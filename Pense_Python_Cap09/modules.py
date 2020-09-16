def palavras_maior_que_vinte(lista):
    for palavra in lista:
        linha = palavra.strip()
        if len(linha) > 20:
            print(linha)


def has_no_letter(lista, letra):
    total_palavras = 0
    palavras_sem_letra = 0

    for palavra in lista:
        linha = palavra.strip()
        total_palavras += 1
        if letra not in linha:
            palavras_sem_letra += 1
            print(linha)

    percentual = (palavras_sem_letra / total_palavras) * 100
    print(f'Total de palavras: {total_palavras}')
    print(f'Total de palavras sem a letra "{letra}": {palavras_sem_letra}')
    print(f'Percentual de palavras sem a letra "{letra}": {percentual:.2f}')


def avoids(letra):
    arquivo = open('words.txt')
    total_de_palavras = 0
    palavras_sem_letra = 0

    for palavra in arquivo:
        linha = palavra.strip()
        total_de_palavras += 1
        for l in letra:
            if l not in linha:
                palavras_sem_letra += 1

    # print(palavras_sem_letra)
    return palavras_sem_letra

    arquivo.close()

# def avoids(lista, letras):
#     tot_letras = 0
#     nao_tem_letra = 0
#     for l in letras:
#         for palavra in lista:
#             linha = palavra.strip()
#             if l in linha:
#                 tot_letras += 1
#             else:
#                 nao_tem_letra += 1

#     print(nao_tem_letra)

#     # if tot_letras == 0:
#     #     return True
