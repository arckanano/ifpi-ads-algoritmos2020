def main():

    print("Inserir valores das variaveis:")
    A = float(input("A = "))
    B = float(input("B = "))
    C = float(input("C = "))


    delta = ((B ** 2) -4 * A * C)

    if A == 0:
        print("Impossivel calcular")
    elif delta < 0:
        print("Impossivel calcular")
    else:
        x1 = (-B + (delta ** (1 / 2))) / (2 * A)
        x2 = (-B - (delta ** (1 / 2))) / (2 * A)
        print("Raiz 1 = {:.5f}".format(x1))
        print("Raiz 2 = {:.5f}".format(x2))


main()
