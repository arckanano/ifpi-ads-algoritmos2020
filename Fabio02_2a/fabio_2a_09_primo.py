def main():

    # n = 101
    n = int(input("Numero: "))
    # numero de divisores
    qtd_divisor=0
    for divisor in range(1, n+1):
        if n % divisor == 0:
            qtd_divisor += 1
            print('divisores: ', divisor)
    # verifica se o numero de divisores, e se for igual a 2 então imprimi a mensagem
    if qtd_divisor > 2:
        print('não é primo')
    else:
        print('é primo')

main()