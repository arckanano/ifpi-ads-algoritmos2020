import tools


def main():

    matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    separador = []

    soma_total = 0
    soma_diagonal_principal = 0
    soma_diagonal_secundaria = 0

    contador = len(matriz)-1

    for l in range(len(matriz)):
        soma_diagonal_secundaria += matriz[l][contador]
        separador.append(matriz[l][contador])
        contador -= 1
        for c in range(len(matriz[l])):
            # soma_total += matriz[l][c]
            if l == c:
                separador.append(matriz[l][c])
                soma_diagonal_principal += matriz[l][c]
            if matriz[l][c] not in separador:
                soma_total += matriz[l][c]

    # soma_do_restante = soma_total - soma_diagonal_principal - soma_diagonal_secundaria
    print(f'Soma diagonal principal = {soma_diagonal_principal}')
    print(f'Soma diagona secundária = {soma_diagonal_secundaria}')
    print(f'Soma do restante = {soma_total}')


main()
# TODO: Falta melhorar
