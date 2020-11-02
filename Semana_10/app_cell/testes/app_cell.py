import dbm
import pickle


def main():

    # cria banco de dados
    celulares_db = dbm.open('celulares', 'c')

    menu = '\n---Base de dados de celulares ---'
    menu += '\n1 - Cadastrar celular'
    menu += '\n2 - Listar celulares'
    menu += '\n3 - Editar cadastro'
    menu += '\n4 - Deletar celular'
    menu += '\n0 - Sair'
    menu += '\n---------------------------------'
    menu += '\nOpção: '

    while True:
        option = int(input(menu))
        if option == 1:
            novo_celular()
        elif option == 2:
            listar_celulares()
        elif option == 3:
            editar_cadastro()
        elif option == 4:
            apagar_cadastro()
        elif option == 0:
            print('Encerrando Programa! Volte Sempre!')
            break
        else:
            print('Opção inválida!')
            input('ENTER to continue!')


def novo_celular():
    banco = dbm.open('celulares', 'c')

    print('Iniciando Novo Cadastro de Celular')
    lista = []

    marca = input('Marca: ')
    modelo = input('Modelo: ')
    processador = input('Processador: ')
    mRam = int(input('RAM: '))
    mRom = int(input('Memória: '))

    # Dicionário com os dados
    celular = {'marca': marca, 'modelo': modelo,
               'processador': processador, 'ram': mRam, 'memoria': mRom}

    # Adicionando o dicionárioa a lista
    lista.append(celular)

    # Adicionando a lista ao banco de dados
    # A chave usada para o cadastro é o modelo do aparelho
    banco[modelo] = pickle.dumps(celular) # <<<<<<<<<<< alterar para lista

    print('--- Celular Cadastrado ---')
    input('-----Pressione ENTER para VOLTAR ao MENU-----')

    banco.close()


def listar_celulares():
    banco = dbm.open('celulares', 'r')

    print(f'Total de aparelhos cadastrados na base: {len(banco)}')

    print('Marca\t\tModelo\t\tProcessador\t\tRam\t\tMemoria')
    for key in banco:
        cell = pickle.loads(banco.get(key))
        marca = cell['marca']
        modelo = cell['modelo']
        processador = cell['processador']
        ram = cell['ram']
        memoria = cell['memoria']
        print(f'{marca}\t\t{modelo}\t\t{processador}\t\t{ram}\t\t{memoria}')
        print('-'*90)

    banco.close()

    print('-----Listagem Finalizada-----')
    input('-----Pressione ENTER para VOLTAR ao MENU-----')


def editar_cadastro():
    banco = dbm.open('celulares', 'c')

    edit = input('Modelo a ser alterado: ')
    a = pickle.loads(banco[edit])

    # Backup dos dados
    bkp_marca = a['marca']
    bkp_modelo = a['modelo']
    bkp_processador = a['processador']
    bkp_ram = a['ram']
    bkp_memoria = a['memoria']

    # deletando a chave
    del(banco[edit])

    # Selecionando item a ser alterado
    while True:
        print('Item a ser alterado:')
        item_para_alterar = int(input('1 - marca\n2 - modelo\n3 - processador\n4 - ram\n5 - memoria\n0 - concluir'))
        if item_para_alterar == 1:
            bkp_marca = input('Novo valor: ')
        elif item_para_alterar == 2:
            bkp_modelo = input('Novo valor: ')
        elif item_para_alterar == 3:
            bkp_processador = input('Novo valor: ')
        elif item_para_alterar == 4:
            bkp_ram = input('Novo valor: ')
        elif item_para_alterar == 5:
            bkp_memoria = input('Novo valor: ')
        elif item_para_alterar == 0:
            break
        else:
            print('ERRO')

    celular = {'marca': bkp_marca, 'modelo': bkp_modelo,
               'processador': bkp_processador, 'ram': bkp_ram, 'memoria': bkp_memoria}

    # Adicionando a lista ao banco de dados
    # A chave usada para o cadastro é o modelo do aparelho
    banco[edit] = pickle.dumps(celular) # <<<<<<<<<<< alterar para lista
    
    banco.close()


def apagar_cadastro():
    banco = dbm.open('celulares', 'c')

    print('Os celulares cadastrados são: ')
    for key in banco:
        cell = pickle.loads(banco.get(key))
        print(cell['modelo'], end=' | ')
    modelo = input('\nQual celular você quer remover: ')

    cell = pickle.loads(banco.get(modelo))
    print(cell)

    # Confirmação
    conf = input('Realmente deseja apagar o modelo? [S/N]: ').upper().strip()
    # Apagando
    if conf == 'S':
        input('Modelo DELETADO!\nPressione ENTER para continuar!')
        del(banco[modelo])
    else:
        input('Pressione ENTER para continuar!')

    banco.close()


main()
