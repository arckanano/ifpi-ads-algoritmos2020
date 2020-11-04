import dbm
import pickle


def novo_celular():
    banco = dbm.open('cadastro_cells', 'c')

    print('Iniciando Novo Cadastro de Celular')

    marca = input('Marca: ').strip()
    modelo = input('Modelo: ').strip()
    mRom = int(input('Memória: '))

    # Validador
    while True:
        if validar_cadastro(modelo) == True:
            print('Aparelho já cadastrado!')
            break
        else:
            celular = {'marca': marca, 'modelo': modelo, 'memoria': mRom}

            banco[modelo] = pickle.dumps(celular)

            print('--- Celular Cadastrado ---')
            input('-----Pressione ENTER para VOLTAR ao MENU-----')
            break

    banco.close()


def validar_cadastro(modelo):
    banco = dbm.open('cadastro_cells', 'r')
    for key in banco:
        item = pickle.loads(banco.get(key))
        if modelo == item['modelo']:
            return True
    return False
    banco.close()
