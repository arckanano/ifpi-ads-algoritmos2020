import modules


def main():
    arquivo = open('words.txt')

    menu = '##### WordPplay #####\n' \
        + '1 - Palavras com + de 20 letras\n' \
        + '2 - Palavras sem alguma letra\n' \
        + '0 - Sair\n' \
        + '\nDigite uma opção: '

    opcao = int(input(menu))

    while opcao != 0:
        if opcao == 1:
            modules.palavras_maior_que_vinte(arquivo)
        elif opcao == 2:
            letra = input('Eu quero as palavras que não tenham a letra: ')
            modules.has_no_letter(arquivo, letra)
        elif opcao == 3:
            print('teste')
        else:
            print('Opção inválida!')

        input('continuar <enter>...')
        opcao = int(input(menu))

    print('Fim Word Play')


main()