def main():

    print("Digite 'F' para Feminino e 'M' para Masculino")
    l = input("Letra: ").upper()

    if l == "F":
        print("Feminino")
    elif l == "M":
        print("Masculino")
    else:
        print("Letra inválida")


main()
