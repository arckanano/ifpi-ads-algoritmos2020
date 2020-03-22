def main():
    '''
    Um número é um quadrado perfeito quando a raiz quadrada do número é igual à soma das dezenas formadas pelos seus dois primeiros e dois últimos dígitos.
    Exemplo: √9801 = 99 = 98 + 01. O número 9801 é um quadrado perfeito.
    Escreva um algoritmo que leia um número de 4 dígitos e verifique se ele é um quadrado perfeito
    '''

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
