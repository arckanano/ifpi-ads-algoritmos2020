def main():

    n = int(input('Valor: '))

    soma = 0
    d = 0
    for i in range(1, n+1):
        print(f'{i}/{n-d}', end=' ')
        if i >= n:
            print('=', end=' ')
        else:
            print('+', end=' ')
        soma += (i/(n-d))
        d += 1
    print(soma)


main()
