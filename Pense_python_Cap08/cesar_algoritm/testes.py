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
        elif numero(letra) == True:
            print(letra, end='')
        elif letra_minuscula(letra) == True:
            virar_minuscula(letra, passo)
        elif letra_maiuscula(letra) == True:
            virar_maiuscula(letra, passo)


def virar_minuscula(letra, passo):
    if (ord(letra) + passo) > 122:
        a = (ord(letra) + passo) - 26
        print(chr(a), end='')
    else:
        print(chr(ord(letra) + passo), end='')


def virar_maiuscula(letra, passo):
    if (ord(letra) + passo) > 90:
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


def numero(letra):
    if (ord(letra) >= 48 and ord(letra) <= 57):
        return True
    else:
        return False


main()
