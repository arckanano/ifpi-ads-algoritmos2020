def main():

    n = int(input('Valor: '))

    soma = 0
    for i in range(1, n+1):
        if i % 2 != 0:
            print('+', end=' ')
            print(f'1/{i}', end=' ')
            soma += (1/i)
        else:
            print('-', end=' ')
            print(f'1/{i}', end=' ')
            soma -= (1/i)

    print(' = ', soma)


main()
