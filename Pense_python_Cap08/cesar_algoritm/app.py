def main():

    '''
    > Cifra de césar
    --- Este código codifica a palavra de acordo com determinado numero de passos que o usuário inserir.
    --- O código não funciona para letras fora do alfabeto latino.
    --- O código não funciona para palavras/letras acentuadas, mesmo que pertençam ao alfabeto latino.
    '''

    palavra = input('Palavra: ')
    passo = int(input('avançar quantas letras? '))

    print('-'*30)
    print('--- SUA PALAVRA CIFRADA ---')

    confere(palavra, passo)


def confere(palavra, passo):
    for letra in palavra:
        if (ord(letra) == 32):
            print(letra, end='')
        elif numero(ord(letra)) == True:
            print(letra, end='')
        elif letra_minuscula(ord(letra)) == True:
            virar_minuscula(ord(letra), passo)
        elif letra_maiuscula(ord(letra)) == True:
            virar_maiuscula(ord(letra)  , passo)


def virar_minuscula(letra, passo):
    if (letra + passo) > 122:
        a = (letra + passo) - 26
        print(chr(a), end='')
    else:
        print(chr(letra + passo), end='')


def virar_maiuscula(letra, passo):
    if (letra + passo) > 90:
        a = (letra + passo) - 26
        print(chr(a), end='')
    else:
        print(chr(letra + passo), end='')


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


def numero(letra):
    if (letra >= 48 and letra <= 57):
        return True
    else:
        return False


main()
