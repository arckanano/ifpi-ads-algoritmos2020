def main():

    print("Digite 5 números diferentes!")
    n1 = int(input("n1: "))
    n2 = int(input("n2: "))
    n3 = int(input("n3: "))
    n4 = int(input("n4: "))
    n5 = int(input("n5: "))

    menor = n1
    maior = n5
    # TESTAR MENOR VALOR
    if n1 < n2 and n1 < n3 and n1 < n4 and n1 < n5:
        print("menor: {}".format(menor))
    if n2 < n1 and n2 < n3 and n2 < n4 and n2 < n5:
        print("menor: {}".format(n2))
    if n3 < n1 and n3 < n2 and n3 < n4 and n3 < n5:
        print("menor: {}".format(n3))
    if n4 < n1 and n4 < n2 and n4 < n3 and n4 < n5:
        print("menor: {}".format(n4))
    if n5 < n1 and n5 < n2 and n5 < n3 and n5 < n4:
        print("menor: {}".format(n5))
    # TESTAR MAIOR VALOR
    if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5:
         print("Maior: {}".format(n1))
    if n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5:
        print("Maior: {}".format(n2))
    if n3 > n1 and n3 > n2 and n3 > n4 and n3 > n5:
        print("Maior: {}".format(n3))
    if n4 > n1 and n4 > n2 and n4 > n3 and n4 > n5:
        print("Maior: {}".format(n4))
    if n5 > n1 and n5 > n2 and n5 > n3 and n5 > n4:
        print("Maior: {}".format(maior))


main()
