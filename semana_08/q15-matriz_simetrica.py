import tools


def main():

    testeMatrizSimetrica = [[1, 5, 9], [5, 3, 8], [9, 8, 7]]

    # Cria uma matriz quadrada aleatoria de ordem N que vai receber os dados da matriz para cálculo
    m1 = tools.cria_matriz_quadrada_aleatoria(3)

    # Criar nova matriz quadrada de ordem N quer será o objeto de cálculo
    # m2 = tools.cria_matriz_quadrada_aleatoria(3)
    m2 = testeMatrizSimetrica
    print('Matriz original para calculo: ')
    for item in m2:
        print(item)

    # Substituir os elementos da primeira matriz pelos elementos da segunda matriz substituindo colunas por linhas
    for i in range(len(m2)):
        for j in range(len(m2[i])):
            m1[i][j] = m2[j][i]

    print('Matriz original transposta:')
    for item in m1:
        print(item)

    print()
    # verificar se a matriz original e a matriz transposta são iguais
    print('são iguais' if m1 == m2 else 'não são iguais')


main()
