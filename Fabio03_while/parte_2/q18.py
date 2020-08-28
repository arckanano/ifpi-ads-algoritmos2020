def main():

    n = int(input('Valor: '))

    contador = 1
    y = 0
    soma = 0
    while contador <= n:
        z = n - y
        x = contador / z
        print(f'{contador} / {z}')
        soma += x
        if x == n:
            break
        y += 1
        contador += 1
    print(f'Resultado: {soma}')


main()
