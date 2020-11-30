def main():

    n1 = float(input("Nota 01: "))
    n2 = float(input("Nota 02: "))

    m = (n1+n2) / 2
    print("-"*10)

    print("primeira nota: {}".format(n1))
    print("segundad nota: {}".format(n2))
    print("Média: {}".format(m))

    if m >= 9 and m <= 10:
        print("Conceito: A")
        print("APROVADO")
    elif m >= 7.5 and m < 9:
        print("Conceito: B")
        print("Aprovado")
    elif m >= 6 and m < 7.5:
        print("Conceito: C")
        print("Aprovado")
    elif m >= 4 and m < 6:
        print("Conceito: D")
        print("Reprovado")
    elif m >= 0 and m < 4:
        print("Conceito: E")
        print("Reprovado")


main()
