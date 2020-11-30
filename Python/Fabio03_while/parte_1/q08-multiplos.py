def main():

    n = int(input('N: '))
    limite_inferior = int(input('Limite inferior: '))
    limite_superior = int(input('Limite superior: '))
    resultado(n, limite_inferior, limite_superior)


def resultado(n, a=1, b=10):
    while (a <= b):
        if a % n == 0:
            print(a)
        a += 1


main()
