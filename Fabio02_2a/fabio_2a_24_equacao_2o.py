import functions

# Leia os coeficientes (A, B e C) de uma equações de 2° grau e escreva suas raízes. Vale lembrar que o coeficiente A deve ser diferente de 0 (zero)

def main():

    print("Inserir valores das variaveis:")
    a = float(input("A = "))
    b = float(input("B = "))
    c = float(input("C = "))

    delta = functions.delta(a, b, c)

    if a == 0:
        print("Impossivel calcular")
    elif delta < 0:
        print("Impossivel calcular")
    else:
        x1 = functions.raiz1(a, b, c)
        x2 = functions.raiz2(a, b, c)
        print(f"Raiz 1 = {x1:.5f}")
        print(f"Raiz 2 = {x2:.5f}")


main()
