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


# def busca_celular():

#     banco = dbm.open('cadastro_cells', 'c')

#     search = input('Busca: ')

#     for key in banco:
#         item = pickle.loads(banco.get(key))
#         if search in item['modelo'] or search in item['marca']:
#             print(item['modelo'])
    
#     menu = '\n---O que fazer agora---'
#     menu += '\n1 - Mostrar detalhes'
#     menu += '\n2 - Editar'
#     menu += '\n3 - Duplicar'
#     menu += '\n4 - Remover'
#     menu += '\n0 - Voltar'
#     menu += '\nOpção: '
#     while True:
#         option = int(input(menu))
#         if option == 1:
#             pass
#         elif option == 2:
#             pass
#         elif option == 3:
#             pass
#         elif option == 4:
#             pass
#         elif option == 0:
#             break
#         else:
#             print('--- OPERAÇÃO INVÁLIDA ---')
#     # selecionar_modelo = input('Selecionar Modelo: ')



#     banco.close()

main()
