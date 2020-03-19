def main():
    # Utilizando o crivo de erastótenes
    n = int(input("numero: "))

    if n == 2 or n == 3 or n == 5:
        print("primo")
    elif n == 0 or n == 1:
        print("não é primo")
    elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0:
        print("nao é primo")
    else:
        print("primo")


main()