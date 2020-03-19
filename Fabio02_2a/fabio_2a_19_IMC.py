def main():

    altura = float(input("Altura: "))
    peso = float(input("Peso: "))

    imc = peso / (altura**2)

    print("IMC: {}".format(imc))

    if imc < 25:
        print("peso normal")
    elif imc >= 25 and imc < 30:
        print("obeso")
    else:
        print("Obesidade morbida")

main()
