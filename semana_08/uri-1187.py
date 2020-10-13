import tools


def main():

    matriz = tools.cria_matriz_quadrada_aleatoria(12)

    for item in matriz:
        print(item)
    print()

    soma = 0
    contador = 0

    c = 1
    k = len(matriz) - 1
    t = (len(matriz) // 2)-1
    for i in range(0, t):
        for j in range(c, k):
            print(matriz[i][j], end=' ')
            soma += matriz[i][j]
            contador += 1
        print()
        c += 1
        k -= 1

    media = soma / contador
    menu = '\nOPERAÇÃO\n1 - SOMA\n2 - MEDIA\n>>> '
    op = int(input(menu))
    if op == 1:
        print(f'A soma dos elementos é: {soma:.1f}')
    elif op == 2:
        print(f'A media dos elementos é: {media:.1f}')


main()
