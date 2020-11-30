def main():
    n1 = float(input("Nota 01: "))
    n2 = float(input("Nota 02: "))

    m = (n1 + n2) / 2

    if m == 10:
        print("Aprovado com distinção")
    elif m >= 7:
        print("Aprovado")
    elif m < 7:
        print("Reprovado")


main()
