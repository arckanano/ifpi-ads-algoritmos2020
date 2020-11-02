def main():

    # mode='r' Leitura apenas, DEFAULT
    # mode='a' ESCRITA, add ao final se o arquivo existir
    # mode='w' ESCRITA, sobrescreve os dados existentes
    # mode='x' Cria um novo arquivo e abre no modo escrita

    menu = '\n--- Opções ---'
    menu += '\n1 - Novo TODO'
    menu += '\n2 - Ver TODOs'
    menu += '\n3 - Editar TODO'
    menu += '\n4 - Excluir TODO'
    menu += '\n0 - Sair'
    menu += '\nOpção > '

    while True:
        option = int(input(menu))
        if option == 1:
            novo_todo()
        elif option == 2:
            ver_todos()
        elif option == 3:
            editar_todo()
        elif option == 4:
            excluir_todo()
        elif option == 0:
            break
        else:
            print('Operação inválida!')
            input('PRESS <ENTER> to CONTINUE')


def novo_todo():
    arquivo = open('todos.txt', mode='a', encoding='utf-8')

    new = input('Nova tarefa: ')
    arquivo.write(f'{new}\n')

    arquivo.close()
    input('PRESS <ENTER> TO CONTINUE')


def ver_todos():
    print('\n Lista de TODOS ')
    arquivo = open('todos.txt', mode='r')

    c = 1
    for linha in arquivo:
        print(f'{c} - {linha}', end='')
        c += 1

    arquivo.close()
    input('PRESS <ENTER> TO CONTINUE')


def editar_todo():
    arquivo = open('todos.txt', mode='r', encoding='utf-8')
    temp_list = []
    for linha in arquivo:
        temp_list.append(linha.rstrip('\n'))
    arquivo.close()

    arquivo = open('todos.txt', mode='w', encoding='utf-8')
    for i in range(len(temp_list)):
        print(f'item {i} - {temp_list[i]}')

    op = int(input('Qual item editar: '))

    temp_list[op] = input('Novo texto: ')

    for item in temp_list:
        arquivo.write(f'{item}\n')

    arquivo.close()
    input('PRESS <ENTER> TO CONTINUE')


def excluir_todo():
    arquivo = open('todos.txt', mode='r', encoding='utf-8')
    temp_list = []
    for linha in arquivo:
        temp_list.append(linha.rstrip('\n'))
    arquivo.close()

    arquivo = open('todos.txt', mode='w', encoding='utf-8')
    for i in range(len(temp_list)):
        print(f'item {i} - {temp_list[i]}')

    op = int(input('Qual item excluir: '))
    temp_list.pop(op)

    for item in temp_list:
        arquivo.write(f'{item}\n')

    arquivo.close()
    input('PRESS <ENTER> TO CONTINUE')


main()
