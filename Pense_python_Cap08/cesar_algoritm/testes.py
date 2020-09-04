def main():

    '''
    > Cifra de césar
    --- Este código codifica a palavra de acordo com determinado numero de passos que o usuário inserir.
    --- O código não funciona para letras fora do alfabeto latino.
    --- O código não funciona para palavras/letras acentuadas, mesmo que pertençam ao alfabeto latino.
    --- Até o momento o código não funciona vira caso seja inserido algum número.
    '''

    palavra = input('Palavra: ')
    passo = int(input('avançar quantas letras? '))

    print('-'*30)
    print('--- SUA PALAVRA CIFRADA ---')

    confere(palavra, passo)


def confere(palavra, passo):
    for letra in palavra:
        if letra_minuscula(letra) == True:
            virar_minuscula(letra, passo)
        if letra_maiuscula(letra) == True:
            virar_maiuscula(letra, passo)
        # elif (ord(letra) + passo) > 122: # Para letras minusculas
        #     a = (ord(letra) + passo) - 26
        #     print(chr(a), end=' ')
        # elif (ord(letra) + passo) > 90:
        #     a = (ord(letra) + passo) - 26
        #     print(chr(a), end=' ')
        # else:
        #     # transforma os códigos de volta em letras já criptografado
        #     print(chr(ord(letra) + passo), end=' ')


def virar_minuscula(letra, passo):
    if letra == ' ':
        print(' ', end='')
    elif (ord(letra) + passo) > 122:  # Para letras minusculas
        a = (ord(letra) + passo) - 26
        print(chr(a), end=' ')
    else:
        print(chr(ord(letra) + passo), end=' ')


def virar_maiuscula(letra, passo):
    if letra == ' ':
        print(' ', end='')
    elif (ord(letra) + passo) > 90:  # Para letras minusculas
        a = (ord(letra) + passo) - 26
        print(chr(a), end=' ')
    else:
        print(chr(ord(letra) + passo), end=' ')



def letra_minuscula(letra):
    if (ord(letra) >= 97 and ord(letra) <= 122):
        return True
    else:
        return False


def letra_maiuscula(letra):
    if (ord(letra) >= 65 and ord(letra) <= 90):
        return True
    else:
        return False


main()
