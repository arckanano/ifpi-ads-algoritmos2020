def main():
    p1 = float(input("Produto 01: "))
    p2 = float(input("Produto 02: "))
    p3 = float(input("Produto 03: "))

    if p1 < p2 and p1 < p3:
        print("compre o produto 01!")
    elif p2 < p1 and p2 < p3:
        print("compre o produto 02!")
    elif p3 < p1 and p3 < p2:
        print("compre o produto 03!")


main()
