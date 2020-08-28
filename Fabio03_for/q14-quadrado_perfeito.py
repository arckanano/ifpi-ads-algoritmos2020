def main():

    n = int(input('N: '))

    for i in range(n, 0, -1):
        # print('i: ', i)
        quadrado = i ** 0.5
        # print('quadrado: ',quadrado)
        if (quadrado % 1) == 0:
            print('perfeito', i)
            break


main()
