def main():

    num = int(input("digite número: "))

    # separando dezena e unidade

    dezena = num // 10
    unidade = num % 10

    # verificação
    if dezena == unidade:
        print("Dezena é igual unidade")
    else:
        print("Dezena é diferente da unidade")


main()
