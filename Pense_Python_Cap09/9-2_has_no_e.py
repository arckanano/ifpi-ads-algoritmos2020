from modules import has_no_letter


def main():

    arquivo = open('words.txt')
    l = input('Eu quero as palavras que não tenham a letra: ')
    has_no_letter(arquivo, l)

    arquivo.close()


main()
