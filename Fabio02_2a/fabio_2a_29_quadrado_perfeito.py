def main():

    num = int(input("Numero de 4 digitos: "))

    raiz = num**(1/2)

    dezena1 = num // 100
    dezena2 = num % 100

    if dezena1 + dezena2 == num**(1/2):
        print("A raiz de num é: %d " % raiz)
        print("A soma de {} com {} é {}".format(dezena1, dezena2, dezena1+dezena2))
        print("portanto é um quadrado perfeito")
    else:
        print("não é quadrado perfeito")


main()
