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


def frase_em_linha(frase):
    nova_frase = ''
    for l in frase:
        if l == ' ':
            nova_frase += '\n'
        else:
            nova_frase += l

    return nova_frase


def not_space(frase):
    nova_frase = ''
    for l in frase:
        if l == ' ':
            nova_frase += ''
        else:
            nova_frase += l
    
    return nova_frase

# def troca_caractere(item, novoItem):
#     return novoItem


def duplica_item(frase):
    nova_frase = ''
    for l in frase:
        for i in range(2):
            nova_frase += l
    
    return nova_frase