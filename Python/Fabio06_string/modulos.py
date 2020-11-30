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


def substitui_numeros(frase):
    numeros = '1234567890'
    nova_frase = ''
    for l in frase:
        if l == '1':
            nova_frase += 'um'
        elif l == '2':
            nova_frase += 'dois'
        elif l == '3':
            nova_frase += 'três'
        elif l == '4':
            nova_frase += 'quatro'
        elif l == '5':
            nova_frase += 'cinco'
        elif l == '6':
            nova_frase += 'seis'
        elif l == '7':
            nova_frase += 'sete'
        elif l == '8':
            nova_frase += 'oito'
        elif l == '9':
            nova_frase += 'nove'
        elif l == '0':
            nova_frase += 'zero'
        else:
            nova_frase += l

    return nova_frase