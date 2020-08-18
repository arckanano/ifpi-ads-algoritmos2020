def main():

    n = int(input("Número: "))
    resultado(n)

def resultado(n):
    perfeito = 0
    while n > 0:
        quadrado = n ** 0.5
        # print(quadrado / 1)
        if quadrado % 1 == 0:
            print(f'{n} - {quadrado}')
            perfeito += 1
            if perfeito == 1:
                break
        n -= 1


main()