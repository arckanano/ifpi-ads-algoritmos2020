def main():

    menu = '*** Brincando com Listas ***'
    menu += '\n 1 - Inserir Valores'
    menu += '\n 2 - Mostrar Valor posição'
    menu += '\n 3 - Remover do Final'
    menu += '\n 4 - Remover do Início'
    menu += '\n 5 - Remover de Posição Específica'
    menu += '\n 6 - Exibir lista atual'
    menu += '\n 7 - Inserir item na posição'
    menu += '\n 8 - Contar Pares'
    menu += '\n 9 - Contar ímpares'
    menu += '\n 10 - Contar Primos' # A fazer
    menu += '\n 11 - Contar Positivos' # A fazer
    menu += '\n 12 - Contar Zerados' # A fazer
    menu += '\n 13 - Média dos valores'
    menu += '\n 14 - Contar ocorrência do valor X' # A fazer
    menu += '\n 15 - Dobrar todos os valores'
    menu += '\n 16 - Dividir todos os valores'
    menu += '\n 17 - Dobrar valores múltiplos de N'
    menu += '\n 18 - Apagar todos os valores'
    menu += '\n 19 - Ordenar a lista (crescente/decrescente)'
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
            item = int(input('Item Inteiro: '))
            inserir_posicao_especifica(lista, pos, item)
        elif opcao == 8:
            conta_pares(lista)
        elif opcao == 9:
            conta_impares(lista)
        # elif opcao == 10:

        # elif opcao == 11:
        # elif opcao == 12:
        elif opcao == 13:
            media(lista)
        elif opcao == 14:
            v = int(input('Número de ocorrência do valor: '))
            conta_valor(lista, v)
        elif opcao == 15:
            dobrar_todos_valores(lista)
        elif opcao == 16:
            n = int(input('Dividir por quanto?: '))
            dividir_todos_valores(lista, n)
        elif opcao == 17:
            n = int(input('Divisor: '))
            dobra_multiplos(lista, n)
        elif opcao == 18:
            apagar_lista(lista)
        elif opcao == 19:
            r = int(input('Invertido?[0] = Não / [1] = Sim: '))
            if r == 0:
                ordenar_lista(lista)
            else:
                ordenar_lista(lista, r=True)

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


def conta_pares(lista):
    pares = 0
    for i in lista:
        if i % 2 == 0:
            pares += 1
    print(f'Total de pares: {pares}')
    
    input('<enter> to continue...')


def conta_impares(lista):
    impares = 0
    for i in lista:
        if i % 2 != 0:
            impares += 1
    print(f'Total de ímpares: {impares}')
    
    input('<enter> to continue...')


def media(lista):
    x = sum(lista) / len(lista)
    print(f'A média dos valores é {x}')
    
    input('<enter> to continue...')

def conta_valor(lista, valor):
    x = lista.count(valor)
    print(f'O valor {valor} aparece {x}x na lista.')

    input('<enter> to continue...')


def dobrar_todos_valores(lista):
    for i in range(len(lista)):
        lista[i] *= 2
    
    print(f'A lista com os valores dobrados {lista}')

    input('<enter> to continue...')


def dividir_todos_valores(lista, num):
    for i in range(len(lista)):
        lista[i] = lista[i] / num
    
    print(f'A lista com os valores dividos é: {lista}')

    input('<enter> to continue...')

def dobra_multiplos(lista, num):
    for i in range(len(lista)):
        if lista[i] % num == 0:
            lista[i] *= 2
    
    print(f'Resultado {lista}')
    input('<enter> to continue...')


def apagar_lista(lista):
    lista.clear()
    print('Todos os valores foram apagados!')

    input('<enter> to continue...')


def ordenar_lista(lista, r=False):
    if r == True:
        lista.sort(reverse=True)
    else:
        lista.sort()
    print(f'Lista ordenada: {lista}')

    input('<enter> to continue...')


main()
