def main():

    n = int(input('Total de números: '))
    resultado(n)


def resultado(n):
    tot = soma = media = 0
    while tot < n:
        numero = int(input('Item: '))
        tot += 1
        soma += tot
        media = soma / tot

    print(f'Soma: {soma}')
    print(f'Média: {media}')


main()
