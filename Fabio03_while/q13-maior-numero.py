def main():

    n = int(input('N: '))
    resultado(n)


def resultado(n):
    tot = maior = 0
    while tot < n:
        item = int(input('Item: '))
        if item > maior:
            maior = item
        tot += 1

    print(f'Maior número: {maior}')
    

main()
