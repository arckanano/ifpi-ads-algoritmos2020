from modules import palavras_maior_que_vinte
def main():

    arquivo = open('words.txt')
    palavras_maior_que_vinte(arquivo)

    arquivo.close()

main()
