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
            nova_frase += caractere
        else:
            nova_frase += l
    
    return nova_frase