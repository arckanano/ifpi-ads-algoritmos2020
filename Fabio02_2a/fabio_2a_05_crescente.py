# 
def main():

    n1 = int(input("Número 01: "))
    n2 = int(input("Número 02: "))
    n3 = int(input("Número 03: "))

    # verificação
    # Caso todos os número sejam diferentes

    if n1 < n2 and n2 < n3:
        print(n1, n2, n3)
    elif n1 < n2 and n3 < n2:
        print(n1, n3, n2)
    elif n1 < n3 and n3 < n2:
        print(n1, n3, n2)
    elif n1 < n3 and n2 < n3:
        print(n1, n2, n3)
    elif n2 < n1 and n1 < n3:
        print(n2, n1, n3)
    elif n2 < n1 and n3 < n1:
        print(n2, n3, n1)
    elif n2 < n3 and n3 < n1:
        print(n2, n3, n1)
    elif n2< n3 and n1 < n3:
        print(n2, n1, n3)
    elif n3 < n2 and n2 < n1:
        print(n3, n2, n1)
    elif n3 < n1 and n1 < n2:
        print(n3, n1, n2)
    elif n3 < n2 and n1 < n2:
        print(n3, n1, n2)
    elif n3 < n1 and n2 < n1:
        print(n3, n2, n1)
    # Caso todos os números sejam iguais
    else:
        print("Os número são iguais")


main()
