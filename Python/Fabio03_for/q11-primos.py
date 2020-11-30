def main():

    limite_inferior = int(input('Limite Inferior: '))
    limite_superior = int(input('Limite superior: '))

    for i in range(limite_inferior, limite_superior+1):
        primo(i)


def primo(n):
    divisor = 0
    for i in range(1, n+1):
        if n % i == 0:
            divisor += 1
    if divisor == 2:
        print(n)


main()
