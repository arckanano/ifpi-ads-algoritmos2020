import tools


def main():

    matriz_q = [[4,5,6],[10,11,12],[7,8,9],[1,2,3]]

    m = sum(matriz_q[0]) # Da pra fazer com FOR, mas iria ficar repetitivo.

    somador = 0 # registra a soma de cada subconjunto
    maior_soma = m
    maior_linha = matriz_q[0]
    menor_soma = m
    menor_linha = matriz_q[0]
    for i in range(len(matriz_q)):
        for j in range(len(matriz_q[i])):
            somador += matriz_q[i][j]
        if somador > maior_soma:
            maior_soma = somador
            maior_linha = matriz_q[i]
        elif somador < menor_soma:
            menor_soma = somador
            menor_linha = matriz_q[i]
        somador = 0

    print(f'A maior_soma é {maior_soma} da linha {maior_linha}')
    print(f'A maior_soma é {menor_soma} da linha {menor_linha}')


main()
