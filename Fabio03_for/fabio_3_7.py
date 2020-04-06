# 7. Leia um número N, some todos os números inteiros entre 1 e N e escreva o resultado obtido.
def main():

    n = int(input("Numero: "))
    print(soma_sequencia(n))

def soma_sequencia(n):
    r = 0
    for i in range(n+1):
        r += i
    return r


main()