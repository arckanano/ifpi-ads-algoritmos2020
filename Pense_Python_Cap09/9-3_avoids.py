from modules import avoids

def main():

    arquivo = 'words.txt'
    r = input('Letras: ')
    resultado = avoids(r)
    print(resultado)


main()
