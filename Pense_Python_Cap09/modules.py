# Opção 1
def palavras_maior_que_vinte(lista):
    for palavra in lista:
        linha = palavra.strip()
        if len(linha) > 20:
            print(linha)


# Opção 2
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


# Opção 3
def avoids(palavra, proibidas):
    for letra in palavra:
        if letra in proibidas:
            return False
    return True


# Opção 4
def uses_only(palavra, letras):
    for l in palavra:
        if l not in letras:
            return False
    return True


# Opção 5
def uses_all(palavra, obrigatorias):
    for letra in obrigatorias:
        if letra not in palavra:
            return False
    return True
