import dbm
import pickle

def main():

    menu = '\n --- Cadastro de Pessoas ---'
    menu += '\n1 - Cadastrar nova pessoa'
    menu += '\n2 - Listar pessoas cadastradas'
    menu += '\n3 - Alterar Cadastro'
    menu += '\n4 - Deletar Cadastro'
    menu += '\n0 - SAIR'
    menu += '\n >>> '

    while True:
        option = int(input(menu))
        if option == 1:
            cadastrar()
        elif option == 2:
            listar()
        elif option == 3:
            pass
        elif option == 4:
            deletar()
        elif option == 0:
            print('Programa encerrado')
            print('Volte Sempre!')
            break
        else:
            print('Operação inválida')


def cadastrar():
    banco = dbm.open('pessoas.db', flag='c')

    nome = str(input('Nome: '))

    # Nova chave
    novo_id = len(banco) + 1

    # inserindo dados
    banco['Pessoa_'+str(novo_id)+'_nome'] = nome

    banco.close()


def listar():
    banco = dbm.open('pessoas.db', flag='r')

    print(len(banco)+1)

    for key in banco:
        print(key.decode(), '<>', banco[key].decode())

    banco.close()


def deletar():
    banco = dbm.open('pessoas.db', flag='c')

    for key in banco:
        banco.pop(key)

    banco.close()

main()
