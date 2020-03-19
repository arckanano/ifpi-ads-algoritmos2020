def main():

    lado1 = int(input("Lado 1: "))
    lado2 = int(input("Lado 2: "))
    lado3 = int(input("Lado 3: "))

    if lado1 == 0 or lado2 == 0 or lado3 == 0:
        print("não existe triangulo de lado 0")
    elif lado1 + lado2 < lado3:
        print("não é triangulo")
    elif lado1 + lado3 < lado2:
        print("não é triangulo")
    elif lado2 + lado3 < lado3:
        print("não é triangulo")
    elif lado1 == lado2 == lado3:
        print("triangulo equilatero")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("isosceles")
    elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
        print("escaleno")


main()
