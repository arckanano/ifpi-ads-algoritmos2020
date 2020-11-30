def main():

    print("Digite 5 números diferentes!")
    n1 = int(input("n1: "))
    n2 = int(input("n2: "))
    n3 = int(input("n3: "))
    n4 = int(input("n4: "))
    n5 = int(input("n5: "))

    lista = [n1, n2, n3, n4, n5]

    print("Menor: {}".format(min(lista)))
    print("MAior: {}".format(max(lista)))

main()
