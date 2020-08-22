def main():

    n = int(input('Valor: '))

    cont = 1
    de_cima = 1
    de_baixo = 1
    soma = 0
    while cont <= n:
        div = de_cima / de_baixo
        soma += div
        # print(f'{de_cima} / {de_baixo} = {soma}') # Exibir cálculos 1 a 1
        de_cima += 2
        de_baixo += 1
        cont += 1

    print(f'soma = {soma}')


main()
