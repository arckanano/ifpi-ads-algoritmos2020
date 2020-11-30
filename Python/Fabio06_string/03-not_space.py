import modulos


def main():
    '''
    Leia uma frase e gere uma nova frase, retirando os espaços entre as palavras.
    '''

    frase = input('frase: ')
    print(modulos.troca_caractere(frase, ' ', ''))


main()
