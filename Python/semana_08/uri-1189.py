import tools


def main():

    matriz = tools.cria_matriz_quadrada_aleatoria(12)

    i = 0
    for item in matriz:
        print(f'{i} > {item}')
        i += 1
    print()

    soma = 0
    contador = 0

    inicio_coluna = 0
    fim_coluna = 0
    inicio_linha = 0
    fim_linha = len(matriz)-1

    for i in range(inicio_linha, fim_linha):
        print(f'{i} > ', end=' ')
        for j in range(inicio_coluna, fim_coluna):
            print(matriz[i][j], end=' ')
            soma += matriz[i][j]
            contador += 1
        print()
        if i < (len(matriz) // 2)-1:
            fim_coluna += 1
        elif i == (len(matriz) // 2)-1:
            fim_coluna += 0
        else:
            fim_coluna -= 1

    media = soma / contador
    menu = '\nOPERAÇÃO\n1 - SOMA\n2 - MEDIA\n>>> '
    op = int(input(menu))
    if op == 1:
        print(f'A soma dos elementos é: {soma:.1f}')
    elif op == 2:
        print(f'A media dos elementos é: {media:.1f}')


main()
