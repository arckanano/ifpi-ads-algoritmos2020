# 1. Leia N e escreva todos os números inteiros de 1 a N.
def main():

    n = int(input("Número: "))
    imprime_sequencia(n)

def imprime_sequencia(n):
    for i in range(1, n+1):
        print(i, end=" ")


main()