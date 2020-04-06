# 5. Leia um número, calcule e escreva seu fatorial.
def main():

    n = int(input("Numero: "))
    print(fatorial(n))
    

def fatorial(numero):
    r = 1
    for i in range(1, numero+1):
        r = r * i
    return r


main()