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
    print(f'Percentual de palavras sem a letra "{letra}": {percentual}')



def avoids(lista, letras):
    count = 0
    for palavra in lista:
        linha = palavra.strip()
        for i in linha:
            for j in letras:
                if j == i:
                    count += 1
        if count == 0:
            print(linha)
