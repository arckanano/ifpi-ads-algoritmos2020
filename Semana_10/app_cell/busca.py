import dbm
import pickle


def busca_celular():

    banco = dbm.open('cadastro_cells', 'c')

    search = input('Busca: ')

    for key in banco:
        item = pickle.loads(banco.get(key))
        if search in item['modelo'] or search in item['marca']:
            print(item['modelo'])

    menu = '\n---O que fazer agora---'
    menu += '\n1 - Mostrar detalhes'
    menu += '\n2 - Editar'
    menu += '\n3 - Duplicar'
    menu += '\n4 - Remover'
    menu += '\n0 - Voltar'
    menu += '\nOpção: '
    while True:
        option = int(input(menu))
        if option == 1:
            selecionar_modelo = input('Selecionar Modelo: ')
            mostrar_detalhes(selecionar_modelo)
            pass
        elif option == 2:
            selecionar_modelo = input('Selecionar Modelo: ')
            pass
        elif option == 3:
            selecionar_modelo = input('Selecionar Modelo: ')
            pass
        elif option == 4:
            selecionar_modelo = input('Selecionar Modelo: ')
            pass
        elif option == 0:
            break
        else:
            print('--- OPERAÇÃO INVÁLIDA ---')

    banco.close()


def mostrar_detalhes(modelo):
    banco = dbm.open('cadastro_cells', 'c')

    item = pickle.loads(banco.get(modelo))
    print(f'MARCA: {item['marca']}\nMODELO: {item['modelo']}\nMEMORIA: {item['memoria']}')
    print(item)

    banco.close()