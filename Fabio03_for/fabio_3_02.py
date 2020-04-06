# 2. Leia N e escreva todos os números inteiros pares de 1 a N.
def main():

    n = int(input("Numero: "))
    retorna_par(n)

def retorna_par(n):
    for i in range(n+1):
        if i % 2 == 0:
            print(i, end=" ")


main()