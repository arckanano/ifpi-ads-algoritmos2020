def cripto():

    numero_de_entradas = int(input('Número de entradas: '))

    contador = 1
    while contador <= numero_de_entradas:
        texto = input('>>> ')

        moved = mover_texto(texto, 3)
        # print('texto movido', moved)
        inverted = inverter_texto(moved)
        # print('Texto Invertido', inverted)
        divided = dividir_texto(inverted)
        print('Resultado: ', divided)

        contador += 1


def mover_texto(texto, casas):
    texto_para_direita = ''
    for letra in texto:
        if letra == ' ':
            texto_para_direita += ' '
        elif letra_minuscula(ord(letra)):
            texto_para_direita += chr(ord(letra) + casas)
        elif letra_maiuscula(ord(letra)):
            texto_para_direita += chr(ord(letra) + casas)
        else:
            texto_para_direita += chr(ord(letra))
    return texto_para_direita


def inverter_texto(texto):
    texto_invertido = ''
    for l in range(len(texto)-1, -1, -1):
        texto_invertido += texto[l]
    return texto_invertido


def dividir_texto(texto):
    primeira_metade = ''
    segunda_metade = ''
    texto_junto = ''

    metade_do_texto = len(texto) / 2
    for letra in range(len(texto)):
        if letra < metade_do_texto:
            primeira_metade += texto[letra]
            # texto_junto += texto[letra] # OBSERVAR
        elif letra >= metade_do_texto:
            segunda_metade += mover_texto(texto[letra], -1)
        texto_junto = primeira_metade + segunda_metade
            # segunda_metade += texto[letra]
    # print('Primeira metade: ', primeira_metade)
    # print('Segunda metade: ', segunda_metade)
    return texto_junto


def letra_minuscula(letra):
    if (letra >= 97 and letra <= 122):
        return True
    else:
        return False


def letra_maiuscula(letra):
    if (letra >= 65 and letra <= 90):
        return True
    else:
        return False

cripto()
