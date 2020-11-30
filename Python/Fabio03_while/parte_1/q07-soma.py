def main():

    n = int(input('Numero: '))

    contador = 1
    soma = 0
    while contador <= n:
        soma += contador
        if contador == n:
            print(f'{contador}', end=' ')
            print('= ', end='')
        else:
            print(f'{contador} +', end=' ')
        contador += 1

    print(f'{soma}')


main()
