def inverte(frase):
    invertida = ''
    for i in range(len(frase)-1, -1, -1):
        invertida += frase[i]

    return invertida


def substitui_consoantes(frase, caractere):
    vogais = 'aeiouAEIOU'
    nova_frase = ''
    for l in frase:
        if l not in vogais:
            nova_frase += '#'
        else:
            nova_frase += l

    return nova_frase


def troca_caractere(frase, item, novoItem):
    nova_frase = ''
    for l in frase:
        if l == item:
            nova_frase += novoItem
        else:
            nova_frase += l

    return nova_frase


def duplica_item(frase):
    nova_frase = ''
    for l in frase:
        for i in range(2):
            nova_frase += l

    return nova_frase
