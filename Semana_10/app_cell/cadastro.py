import dbm
import pickle


def novo_celular():
    banco = dbm.open('cadastro_cells', 'c')

    print('Iniciando Novo Cadastro de Celular')

    marca = input('Marca: ')
    modelo = input('Modelo: ')
    mRom = int(input('Memória: '))

    # Dicionário com os dados
    celular = {'marca': marca, 'modelo': modelo, 'memoria': mRom}

    # Adicionando a lista ao banco de dados
    # A chave usada para o cadastro é o modelo do aparelho
    banco[modelo] = pickle.dumps(celular)  # <<<<<<<<<<< alterar para lista

    print('--- Celular Cadastrado ---')
    input('-----Pressione ENTER para VOLTAR ao MENU-----')

    banco.close()
