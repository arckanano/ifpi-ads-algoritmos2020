import tools


def main():

    matriz = tools.cria_matriz_quadrada_aleatoria(12)

    for item in matriz:
        print(item)
    print()

    soma = 0
    contador = 0

    c = len(matriz)-1
    for i in range(1, len(matriz)-1):
        for j in range(c, len(matriz[i])):
            print(matriz[i][j], end=' ')
            soma += matriz[i][j]
            contador += 1
        c -= 1

    media = soma / contador
    menu = '\nOPERAÇÃO\n1 - SOMA\n2 - MEDIA\n>>> '
    op = int(input(menu))
    if op == 1:
        print(f'A soma dos elementos é: {soma:.1f}')
    elif op == 2:
        print(f'A media dos elementos é: {media:.1f}')


main()
