def main():

    n = int(input('Número de termos: '))

    inicio = 1
    contador = 1
    razao = 2
    while contador <= n:
        print(inicio)
        inicio += razao
        razao += 1
        contador += 1


main()
