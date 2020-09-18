import modulos


def main():

    frase = input('Frase: ')
    caractere = '#'

    frase_invertida = modulos.inverte(frase)

    sem_consoante = modulos.substitui_consoantes(frase_invertida, caractere)
    print(sem_consoante)

    
main()
