import modules


def main():
    arquivo = open('words.txt')

    menu = '##### WordPplay #####\n' \
        + '1 - Palavras com + de 20 letras\n' \
        + '2 - Palavras sem alguma letra\n' \
        + '3 - Palavras sem várias letras\n' \
        + '4 - Palavras somente com as letras da lista\n' \
        + '5 - Palavras com todas as letras da lista\n' \
        + '6 - Palavras com letras em ordem alfabética\n' \
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
            letras = input('Palavras sem as letras: ')
            modules.avoids(arquivo, letras)
        elif opcao == 4:
            modules.uses_only(palavra, letras)
        elif opcao == 5:
            modules.uses_all(palavra, letras)
        else:
            print('Opção inválida!')

        input('continuar <enter>...')
        opcao = int(input(menu))

    print('Fim Word Play')


main()