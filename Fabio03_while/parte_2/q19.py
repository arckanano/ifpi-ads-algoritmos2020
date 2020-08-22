def main():

    n = int(input('valor: '))

    contador = 1
    soma = 0
    while n >= 1:
        if contador % 2 == 0:
            print(f'-({contador} / {n})', end=' ')
            soma -= (contador / n)
        else:
            print(f'+({contador} / {n})', end=' ')
            soma += (n / contador)
        n -= 1
        contador += 1
    print(f'Soma = {soma}')


main()
