def main():

    n = int(input('Quantidade de itens: '))

    contador = 1
    soma = 0
    while contador <= n:
        s = 1 / contador
        soma += s
        contador += 1
    print(f'resultado = {soma}')


main()
