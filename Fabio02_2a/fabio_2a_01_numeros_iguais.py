def main():

    num1 = int(input("Número 01: "))
    num2 = int(input("Número 02: "))
    num3 = int(input("Número 03: "))

    if num1 == num2:
        print("2 números iguais")
    elif num1 == num3:
        print("2 números iguais")
    elif num2 == num3:
        print("2 número iguais")
    elif num1 == num2 == num3:
        print("3 números iguais")
    else:
        print("sem números iguais")


main()