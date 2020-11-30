def main():

    n = int(input('N: '))

    soma = 0
    for i in range(n):
        valor = int(input('Valor: '))
        soma += valor
    media = soma / n
    print(f'SOMA = {soma} | MEDIA = {media}')


main()
