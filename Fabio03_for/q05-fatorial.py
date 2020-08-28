def main():

    n = int(input('Número: '))

    fat = 1
    for i in range(n, 1, -1):
        fat *= i
    print(f'Fatorial de {n} = {fat}')


main()
