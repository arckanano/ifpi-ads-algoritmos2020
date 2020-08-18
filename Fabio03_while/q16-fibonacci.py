def main():

    n = int(input('Número de termos: '))

    contador = 0
    a = 0
    b = 1
    while contador <= n:
        print(a)
        c = a+b
        # a = b
        # b = c
        a,b = b,c
        contador += 1

main()