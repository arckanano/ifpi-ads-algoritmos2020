# Objetivo 1: criar um arquivo que é um banco de dados e adicionar itens nele.
# Objetivo 2: recuperar o arquivo que é o banco de dados e adicionar novos itens nele.
def main():

    menu = '\n--- APP FRUTERIA ---'
    menu += '\n 1 - Adicionar Fruta'    # Create
    menu += '\n 2 - Listar Frutas'      # Read
    menu += '\n 3 - Renomear Fruta'     # Update
    menu += '\n 4 - Apagar Fruta'       # Delete
    menu += '\n 0 - Sair'
    menu += '\n\n Opção > '

    fruteira = ['abacate', 'maçã', 'abacaxi', 'laranja']

    while True:
        option = int(input(menu))
        if option == 1:
            nova_fruta(fruteira)
        elif option == 2:
            listar_itens(fruteira)
        elif option == 3:
            alterar_fruta(fruteira)
        elif option == 4:
            apagar_fruta(fruteira)
        elif option == 0:
            print('--- Obrigado e volte sempre ---')
            break
        else:
            print('Operação inválida')
            input('Pressione <ENTER> para continuar')


def nova_fruta(fruteira):
    fruta = input('Fruta: ')
    if verificar_existencia(fruta, fruteira):
        print('Fruta já existe!')
    else:
        fruteira.append(fruta)

    print('Operação concluida')
    input('Pressione <ENTER> para continuar')


def verificar_existencia(fruta, fruteira):
    for f in fruteira:
        if fruta == f:
            return True
    return False


def listar_itens(fruteira):
    c = 1
    for f in range(len(fruteira)):
        print(f'{c} - {fruteira[f]}')
        c += 1

    print('Operação concluida')
    input('Pressione <ENTER> para continuar')


def alterar_fruta(fruteira):
    print('As frutas existente são: ')

    c = 1
    for i in range(len(fruteira)):
        print(f'{c} - {fruteira[i]}')
        c += 1

    print('Qual você deseja alterar?')
    option = int(input(''))

    fruteira[option-1] = input('Nova Fruta: ')

    print('Operação concluida')
    input('Pressione <ENTER> para continuar')


def apagar_fruta(fruteira):
    print('Suas frutas são essas: ')
    c = 1
    for i in range(len(fruteira)):
        print(f'{c} - {fruteira[i]}', end=' ')
        c += 1

    item = int(input('\nQual fruta deseja apagar: '))
    fruteira.pop(item-1)
    
    print('\nOperação concluida')
    input('Pressione <ENTER> para continuar')


main()
