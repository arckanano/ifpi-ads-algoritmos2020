def main():
    p1 = float(input("Produto 01: "))
    p2 = float(input("Produto 02: "))
    p3 = float(input("Produto 03: "))

    l_p = [p1, p2, p3]

    print("Compre o produto: {}".format(min(l_p)))


main()
