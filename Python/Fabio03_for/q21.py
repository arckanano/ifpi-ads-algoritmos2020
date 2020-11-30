def main():

    n = int(input('Valor: '))

    soma = 0
    divisor = 1
    for i in range(1, n+1):
        print(f'{divisor}/{i}', end=' ')
        if i >= n:
            print('=', end=' ')
        else:
            print('+', end=' ')
        soma += (divisor / i)
        divisor += 2
    print(soma)


main()
