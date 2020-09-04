def main():

    palavra = input('Palavra: ')
    passo = int(input('avançar quantas letras? '))

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
