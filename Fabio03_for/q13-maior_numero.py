def main():

    n = int(input('Quantidade de itens: '))
    maior = 0
    for i in range(n):
        item = int(input('Item: '))
        if item > maior:
            maior = item
    print(f'maior = {maior}')


main()
