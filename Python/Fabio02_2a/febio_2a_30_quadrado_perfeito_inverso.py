def main():

    num = int(input("Numero de 4 digitos: "))

    dezena1 = num // 100
    dezena2 = num % 100

    soma = dezena1 + dezena2

    teste = (dezena1+dezena2)**2

    if teste == num:
        print("dividindo: {} e {}".format(dezena1, dezena2))
        print("somando: %d" % soma)
        print("quadrado: %d" % teste)
        print("caso aceito")
    else:
        print("dividindo: {} e {}".format(dezena1, dezena2))
        print("somando: %d" % soma)
        print("quadrado: %d" % teste)
        print("caso não aceito")


main()
