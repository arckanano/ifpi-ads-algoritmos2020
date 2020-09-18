import modulos


def main():
    '''
    Leia uma frase e mostre cada palavra da frase em uma linha separada.
    '''

    frase = input('Frase: ')
    r = modulos.troca_caractere(frase, ' ', '\n')
    print(r)


main()
