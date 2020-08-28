def main():

    limite_inferior = int(input('Limite Inferior: '))
    limite_superior = int(input('Limite superior: '))

    for i in range(limite_inferior, limite_superior+1):
        if i % 2 != 0:
            print(i)

main()
