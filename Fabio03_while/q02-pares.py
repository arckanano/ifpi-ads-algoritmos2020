def main():

    numero = int(input('Número: '))

    contador = 0
    while contador <= numero:
        if contador % 2 == 0:
            print(contador)
        contador += 1


main()