def main():

    num1 = int(input("Número 1: "))
    num2 = int(input("Número 2: "))
    num3 = int(input("Número 3: "))

    if num1 > num2 and num1 > num3:
        print("numero 01 é o maior")
    elif num2 > num1 and num2 > num3:
        print("numero 02 é o maior")
    elif num3 > num1 and num3 > num2:
        print("numero 03 é o maior")
    else:
        print("os números são iguais!")


main()
