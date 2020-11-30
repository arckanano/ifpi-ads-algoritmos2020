# 
def main():

    ang1 = int(input("ang1: "))
    ang2 = int(input("ang2: "))
    ang3 = int(input("ang3: "))

    if ang1 + ang2 + ang3 == 180:
        graus = ang1 + ang2 + ang3
        print("A soma dos graus é", graus, "então é triangulo")
        if ang1 < 90 and ang2 < 90 and ang3 < 90:
            print("é um  triângulo acutangulo")
        elif ang1 == 90 or ang2 == 90 or ang3 == 90:
            print("é um  triângulo triangulo retangulo")
        elif ang1 > 90 or ang2 > 90 or ang3 > 90:
            print("é um  triângulo obtusangulo")
    else:
        print("nao é um triangulo")


main()
