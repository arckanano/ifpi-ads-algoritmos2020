def main():

    menu = '*** Brincando com Listas ***'
    menu += '\n 1 - Inserir Valores'
    menu += '\n 2 - Mostrar Valor posição'
    menu += '\n 3 - Remover do Final'
    menu += '\n 4 - Remover do Início'
    menu += '\n 5 - Remover de Posição Específica'
    menu += '\n 6 - Exibir lista atual'
    menu += '\n 7 - Inserir item na posição'
    menu += '\n N - <Crie diversas opções com os dados> '
    menu += '\n 0 - Sair '
    menu += '\n\n Opção >>> '

    lista = []

    while True:
        opcao = int(input(menu))

        if opcao == 1:
            inserir_valores(lista)
        elif opcao == 2:
            mostra_valor(lista)
        elif opcao == 3:
            remove_ultimo_item(lista)
        elif opcao == 4:
            remove_primeiro_item(lista)
        elif opcao == 5:
            pos = int(input('Remover item de qual posição?: '))
            remove_posicao(lista, pos)
        elif opcao == 6:
            exibir_lista(lista)
        elif opcao == 7:
            pos = int(input('Posição: '))
            item = input('Item: ')
            inserir_posicao_especifica(lista, pos, item)

        elif opcao == 0:  # sair do while
            break
        else:
            print('Opção Inválida')


def inserir_valores(lista):
    qtd = int(input('Quantos valores desejar inserir?'))

    for i in range(qtd):
        valor = int(input('Valor: '))
        lista.append(valor)

    print('Valores inseridos com sucesso!')
    input('<enter> to continue...')


def mostra_valor(lista):
    posicao = int(input('Qual posição? '))
    print('Valor buscado:')
    print(lista[posicao])

    input('<enter> to continue...')


def remove_ultimo_item(lista):
    print('Removendo último item')
    lista.pop()
    print(lista)

    input('<enter> to continue...')

def remove_primeiro_item(lista):
    print('Removendo primeiro item')
    lista.pop(0)
    print(lista)

    input('<enter> to continue...')

def remove_posicao(lista, pos):
    print(lista)
    print(f'Removendo item da posição {pos}')
    lista.pop(pos)
    print(lista)

    input('<enter> to continue...')


def exibir_lista(lista):
    print(lista)

    input('<enter> to continue...')


def inserir_posicao_especifica(lista, posicao, item):
    lista.insert(posicao, item)
    print('Itens Inseridos com sucesso!')

    input('<enter> to continue...')

    
main()
