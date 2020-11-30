def main():

    quad = int(input("Angulo: "))

    if quad >= 0 and quad < 90:
        print("Primeiro quadrante")
    elif quad >= 90 and quad < 180:
        print("Segundo quadrante")
    elif quad >= 180 and quad < 270:
        print("Terceiro quadrante")
    elif quad >= 270 and quad < 360:
        print("Quarto qudrante")


main()
