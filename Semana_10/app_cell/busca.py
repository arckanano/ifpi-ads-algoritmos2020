import dbm
import pickle


def busca_celular():

    banco = dbm.open('cadastro_cells', 'c')

    search = input('Buscar por: ')

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
            editar_cadastro(selecionar_modelo)
            pass
        elif option == 3:
            selecionar_modelo = input('Selecionar Modelo: ')
            duplicar_cadastro(selecionar_modelo)
            pass
        elif option == 4:
            selecionar_modelo = input('Selecionar Modelo: ')
            remover_item(selecionar_modelo)
            pass
        elif option == 0:
            break
        else:
            print('--- OPERAÇÃO INVÁLIDA ---')

    banco.close()


def mostrar_detalhes(modelo):
    banco = dbm.open('cadastro_cells', 'c')

    item = pickle.loads(banco[modelo])
    marca = item['marca']
    modelo = item['modelo']
    memoria = item['memoria']
    print(f'Marca = {marca} | Modelo = {modelo} | Memoria = {memoria}GB')

    banco.close()


def remover_item(modelo):
    banco = dbm.open('cadastro_cells', 'c')

    item = pickle.loads(banco[modelo])

    confirm = input(
        'Tem certeza que deseja remover o Modelo selecionado?\nO processo não pode ser desfeito [S|N]').upper()
    if confirm == 'S':
        del(banco[modelo])

    print(' - - - MODELO APAGADO DA BASE - - - ')

    banco.close()


def editar_cadastro(modelo):
    mostrar_detalhes(modelo)

    banco = dbm.open('cadastro_cells', 'c')

    # edit = input('Modelo a ser alterado: ')
    a = pickle.loads(banco[modelo])

    # Backup dos dados
    bkp_marca = a['marca']
    bkp_modelo = a['modelo']
    bkp_memoria = a['memoria']

    # deletando a chave
    del(banco[modelo])

    # Selecionando item a ser alterado
    while True:
        print('Item a ser alterado:')
        item_para_alterar = int(
            input('1 - marca\n2 - modelo\n3 - memoria\n0 - concluir'))
        if item_para_alterar == 1:
            bkp_marca = input('Novo valor: ')
        elif item_para_alterar == 2:
            bkp_modelo = input('Novo valor: ')
        elif item_para_alterar == 3:
            bkp_memoria = input('Novo valor: ')
        elif item_para_alterar == 0:
            break
        else:
            print('ERRO')

    celular = {'marca': bkp_marca,
               'modelo': bkp_modelo, 'memoria': bkp_memoria}

    # Adicionando a lista ao banco de dados
    # A chave usada para o cadastro é o modelo do aparelho
    banco[modelo] = pickle.dumps(celular)  # <<<<<<<<<<< alterar para lista

    banco.close()


def duplicar_cadastro(modelo):
    mostrar_detalhes(modelo)

    banco = dbm.open('cadastro_cells', 'c')

    # edit = input('Modelo a ser alterado: ')
    a = pickle.loads(banco[modelo])

    # Backup dos dados
    bkp_marca = a['marca']
    bkp_modelo = a['modelo']
    bkp_memoria = a['memoria']




    # Adicionando a lista ao banco de dados
    # A chave usada para o cadastro é o modelo do aparelho
    c = 1
    for key in banco:
        if banco[modelo] == banco[key]:
            c += 1
    
    nome_da_chave = f'{modelo}{c}'
    
    # print('C', c)
    celular = {'marca': bkp_marca,
               'modelo': nome_da_chave, 'memoria': bkp_memoria}
    banco[nome_da_chave] = pickle.dumps(celular)  # <<<<<<<<<<< alterar para lista

    banco.close()
