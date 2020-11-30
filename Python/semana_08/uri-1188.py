import tools


def main():

    matriz = tools.cria_matriz_quadrada_aleatoria(12)

    for item in matriz:
        print(item)
    print()

    soma = 0
    contador = 0

    inicio_coluna = (len(matriz) // 2) - 1
    fim_coluna = (len(matriz) // 2)+1

    inicio_linha = (len(matriz) // 2) + 1

    for i in range(inicio_linha, len(matriz)):
        for j in range(inicio_coluna, fim_coluna):
            print(matriz[i][j], end=' ')
            soma += matriz[i][j]
            contador += 1
        print()
        inicio_coluna -= 1
        fim_coluna += 1

    media = soma / contador
    menu = '\nOPERAÇÃO\n1 - SOMA\n2 - MEDIA\n>>> '
    op = int(input(menu))
    if op == 1:
        print(f'A soma dos elementos é: {soma:.1f}')
    elif op == 2:
        print(f'A media dos elementos é: {media:.1f}')


main()
