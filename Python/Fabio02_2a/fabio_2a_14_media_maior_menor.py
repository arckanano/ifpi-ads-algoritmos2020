def main():

    n1 = int(input("n1: "))
    n2 = int(input("n2: "))
    n3 = int(input("n3: "))
    n4 = int(input("n4: "))
    n5 = int(input("n5: "))

    media = (n1+n2+n3+n4+n5) / 5
    lista = [n1, n2, n3, n4, n5]

    for i in lista:
        if media < i:
            print(i)
    print("media: ", media)


main()
