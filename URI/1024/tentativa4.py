def cripto():

    numero_de_entradas = int(input())

    contador = 1
    while contador <= numero_de_entradas:
        texto = input()

        moved = mover_texto(texto, 3)
        inverted = inverter_texto(moved)
        first_half = primeira_metade(inverted)
        second_half = segunda_metade(inverted)
        second_half_moved = mover_texto_basico(second_half)
        together = first_half + second_half_moved
        print(together)
        contador += 1

# Parte 1: Mover MAIUSCULAS E MINUSCULAS 3 casas para a direita


def mover_texto(texto, casas):
    texto_para_direita = ''
    for letra in texto:
        if letra_minuscula(ord(letra)):
            texto_para_direita += chr(ord(letra) + casas)
        elif letra_maiuscula(ord(letra)):
            texto_para_direita += chr(ord(letra) + casas)
        else:
            texto_para_direita += chr(ord(letra))
    return texto_para_direita

# Parte 2: Inverter o texto


def inverter_texto(texto):
    texto_invertido = ''
    for l in range(len(texto)-1, -1, -1):
        texto_invertido += texto[l]
    return texto_invertido

# Divide o Texto e retorna a Primeira metade


def primeira_metade(texto):
    primeira_metade = ''
    metade_do_texto = len(texto) // 2
    for letra in range(len(texto)):
        if letra < metade_do_texto:
            primeira_metade += texto[letra]
    return primeira_metade

# Divide o Texto e retorna a Segunda metade


def segunda_metade(texto):
    segunda_metade = ''
    metade_do_texto = len(texto) // 2
    for letra in range(len(texto)):
        if letra >= metade_do_texto:
            segunda_metade += texto[letra]
    return segunda_metade


def mover_texto_basico(texto):
    txt_movido = ''
    for letra in texto:
        if letra == ' ':
            txt_movido += ' '
        else:
            txt_movido += chr(ord(letra) - 1)
    return txt_movido


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
