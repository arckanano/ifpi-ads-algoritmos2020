import functions

def main():

    altura = float(input("Altura: "))
    peso = float(input("Peso: "))

    #imc = functions.divide2(peso, (altura**2)) # usar função divide2 do módulo functions
    imc = functions.calculo_imc(altura, peso)
    print(f"IMC: {imc}")

'''
    if imc < 25:
        print("peso normal")
    elif imc >= 25 and imc < 30:
        print("obeso")
    else:
        print("Obesidade morbida")
'''
main()
