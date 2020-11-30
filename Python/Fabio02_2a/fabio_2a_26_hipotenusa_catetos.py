def main():
    '''
    Leia os 3 (três) lados de um triângulo e identifique sua hipotenusa e seus catetos
    '''

    lado1 = int(input("Lado 1: "))
    lado2 = int(input("Lado 2: "))
    lado3 = int(input("Lado 3: "))

    if lado1 >= lado3 + lado2:
        print("Hipotenusa: {}\nCateto: {}\nCateto: {}".format(lado1, lado2, lado3))
    elif lado2 >= lado1 + lado3:
        print("Hipotenusa: {}\nCateto: {}\nCateto: {}".format(lado2, lado1, lado3))
    elif lado3 >= lado1 + lado2:
        print("Hipotenusa: {}\nCateto: {}\nCateto: {}".format(lado3, lado2, lado1))

main()
