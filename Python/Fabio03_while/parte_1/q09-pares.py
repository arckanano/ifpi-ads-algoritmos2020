def main():

    limite_inferior = int(input('Limite inferior: '))
    limite_superior = int(input('Limite superior: '))
    resultado(limite_inferior, limite_superior)


def resultado(a=1, b=10):
    while (a <= b):
        if a % 2 == 0:
            print(a)
        a += 1


main()
