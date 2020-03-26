# escreva uma função compare que receba dois valores, x e y, e retorne 1 se x > y, 0 se x == y e -1 se x < y
def main():

    x = int(input("X: "))
    y = int(input("Y: "))
    r = verifica(x, y)
    print(r)


def verifica(x, y):
    if x > 1:
        return 1
    elif x == y:
        return 0
    else:
        return -1


main()