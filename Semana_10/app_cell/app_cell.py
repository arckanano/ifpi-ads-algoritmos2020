import dbm
import pickle

# Módulo dbm
# open(fiel,flags='')
# Tipos de flag
# flag='r' > default, apenas leitura de db existente.
# flag='w' > abre para leitura e escrita de db existente.
# flag='c' > Cria um novo db e abre pra leitura e escrita, caso não existe db. Caso exista db, retorna erro.
# flag='n' > Sempre cria um novo db, mesmo já existindo um. Leitura e escrita.


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
            novo_celular(celulares_db)
        elif option == 2:
            listar_celulares()
        elif option == 3:
            pass
        elif option == 4:
            apagar_cadastro()
        elif option == 0:
            print('Encerrando Programa! Volte Sempre!')
            break
        else:
            print('Opção inválida!')
            input('ENTER to continue!')


def novo_celular(banco):
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
    banco[modelo] = pickle.dumps(lista)

    print('--- Celular Cadastrado ---')
    input('-----Pressione ENTER para VOLTAR ao MENU-----')

    banco.close()


def listar_celulares():
    banco = dbm.open('celulares', 'r')

    print(f'Total de aparelhos cadastrados na base: {len(banco)}')

    filtro = input('Filtro (marca|modelo|processador|ram|memoria): ')
    if filtro == '':
        filtro = 'modelo'

    for key in banco:
        cell = pickle.loads(banco.get(key))
        print(cell[0][filtro])

    banco.close()

    print('-----Listagem Finalizada-----')
    input('-----Pressione ENTER para VOLTAR ao MENU-----')



def editar_cadastro():
    banco = dbm.open('celulares', 'c')

    

    banco.close()
    pass


def apagar_cadastro():
    banco = dbm.open('celulares', 'c')

    print('Os celulares cadastrados são: ')
    for key in banco:
        cell = pickle.loads(banco.get(key))
        print(cell[0]['modelo'], end=' | ')
    modelo = input('\nQual celular você quer remover: ')

    cell = pickle.loads(banco.get(modelo))
    print(cell)

    # Apagando
    del(banco[modelo])

    banco.close()


main()
