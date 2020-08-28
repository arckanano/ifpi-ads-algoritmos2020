def main():

    n = int(input('Valor: '))

    soma = 0
    d = 0
    for i in range(1, n+1):
        elif i % 2 != 0:
            print('+', end=' ')
            print(f'{i}/{n-d}', end=' ')
            soma += (i/(n-d))
        else:
            print('-', end=' ')
            print(f'{n-d}/{i}', end=' ')
            soma -= ((n-d)/i)
        d += 1
    print(' = ', soma)


main()
