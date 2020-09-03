def main():

    palavra = input('Palavra: ')
    passo = int(input('avançar quantas letras? '))

    # for letra in palavra:
    #     print(letra, end='')  # teste para saber se está tudo funcionando

    # for letra in palavra:
    #     print(ord(letra), end=' ')  # Pegar código equivalente na tabela ASCII

    # for letra in palavra: # avança determinado número de caracteres
    #     print(ord(letra) + passo, end=' ')

    print('-'*30)
    print('--- SUA PALAVRA CIFRADA ---')
    for letra in palavra:
        if letra == ' ':
            print(' ', end='')
        elif (ord(letra) + passo) > 122:
            a = ord(letra) + passo
            b = a - 122
            c = b + 96
            print(chr(c), end=' ')
        else:
            # transforma os códigos de volta em letras já criptografado
            print(chr(ord(letra) + passo), end=' ')


main()
