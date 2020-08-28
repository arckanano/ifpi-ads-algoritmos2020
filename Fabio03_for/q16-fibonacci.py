def main():

    n = int(input('Número de termos: '))

    a = 0
    b = 1
    for i in range(n):
        c = a+b
        print(a, end=' ')
        a = b
        b = c


main()
