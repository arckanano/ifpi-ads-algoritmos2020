def main():

    n = int(input('Número de termos: '))

    somador = 1
    acumula = 1
    for i in range(n):
        print(f'{somador}', end=' ')
        acumula += 1
        somador += acumula


main()
