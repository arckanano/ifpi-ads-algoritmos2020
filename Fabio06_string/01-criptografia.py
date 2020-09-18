import modulos


def main():
    caractere = '#'

    frase = input('Frase: ')

    frase_invertida = modulos.inverte(frase)
    sem_consoante = modulos.substitui_consoantes(frase_invertida, caractere)
    print(sem_consoante)


main()
