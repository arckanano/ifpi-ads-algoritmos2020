import dbm
import pickle
import cadastro
import busca


def main():

    celulares_db = dbm.open('cadastro_cells', 'c')

    menu = '\n---App Celular---'
    menu += '\n1 - Cadastrar novo celular'
    menu += '\n2 - Buscar/Listar Celulares'
    menu += '\n0 - Sair'
    menu += '\nOpção: '

    while True:
        option = int(input(menu))
        if option == 1:
            cadastro.novo_celular()
        elif option == 2:
            busca.busca_celular()
        elif option == 0:
            print('Encerrando programa!')
            break
        else:
            print('Opção inválida!')


main()
