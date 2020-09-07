def cripto():

    numero_de_entradas = int(input('Número de entradas: '))

    contador = 1
    while contador <= numero_de_entradas:
        texto = input('>>> ')
        to_right = mover_para_direita(texto)
        inverted = inverter_texto(to_right)
        move_half = codificar(inverted)
        print('move half:', move_half)

        contador += 1


def mover_para_direita(texto):
    texto_para_direita = ''
    for letra in texto:
        texto_para_direita += chr(ord(letra) + 3)
    return texto_para_direita


def inverter_texto(texto):
    texto_invertido = ''
    for l in range(len(texto)-1, -1, -1):
        texto_invertido += texto[l]
    return texto_invertido


def mover_para_esquerda(texto):
    texto_para_esquerda = ''
    for letra in texto:
        texto_para_esquerda += chr(ord(letra) - 1)
    return texto_para_esquerda


def codificar(texto):
    primeira_metade = ''
    segunda_metade = ''
    texto_junto = ''
    metade_do_texto = len(texto) // 2
    for letra in range(len(texto)):
        if letra < metade_do_texto:
            primeira_metade += texto[letra]
            texto_junto += texto[letra] # OBSERVAR
        else:
            segunda_metade += mover_para_esquerda(texto[letra])
            texto_junto += mover_para_esquerda(texto[letra])
            # segunda_metade += texto[letra]
    print('Primeira metade: ', primeira_metade)
    print('Segunda metade: ', segunda_metade)
    return texto_junto


cripto()
