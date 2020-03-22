import functions

def main():

    altura = float(input("Altura: "))
    peso = float(input("Peso: "))

    imc = functions.calculo_imc(altura, peso)
    # print(f"IMC: {imc}")


main()
