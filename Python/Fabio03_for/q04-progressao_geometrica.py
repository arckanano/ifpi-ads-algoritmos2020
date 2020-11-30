def main():

    a_zero = int(input('A0 = '))
    limite = int(input('Limite: '))
    r = int(input('Razão: '))

    for i in range(a_zero, limite, r):
        print(f'{a_zero}')
        a_zero *= r
        if a_zero > limite:
            break


main()
