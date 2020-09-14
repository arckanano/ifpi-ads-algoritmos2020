def palavras_maior_que_vinte(lista):
    for palavra in lista:
        linha = palavra.strip()
        if len(linha) > 20:
            print(linha)


def has_no_letter(lista, letra):
    for palavra in lista:
        linha = palavra.strip()
        if letra not in linha:
            print(linha)


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
