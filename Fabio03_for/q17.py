def main():

    n = int(input('N: '))

    soma = 0
    for i in range(1, n+1):
        print(f'1/{i}', end=' ')
        if i >= n:
            print('=', end=' ')
        else:
            print('+', end=' ')
        soma += (1/i)

    print(soma)


main()
