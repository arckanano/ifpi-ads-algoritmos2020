def main():

    n = int(input('valor: '))

    contador = 1
    s = 0
    while contador <= n:
        d = 1 / contador
        if contador % 2 == 0:
            s -= d
        else:
            s += d
        contador += 1
    print(f'S = {s}')


main()
