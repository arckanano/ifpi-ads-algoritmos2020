from modules import avoids


def main():

    arquivo = open('words.txt')
    l = input('Eu quero as palavras que não tenham a letra: ')
    avoids(arquivo, l)

    arquivo.close()


main()
