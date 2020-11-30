def main():

    n = int(input('Quantidade de habitantes: '))

    soma_salario = 0
    total_filhos = 0
    salario_ate_mil = 0
    for i in range(1, n+1):
        salario = int(input('Seu salário: '))
        qtd_filhos = int(input('Quantidade de filhos: '))
        soma_salario += salario
        total_filhos += qtd_filhos
        if salario <= 1000:
            salario_ate_mil += 1
        print()
    media_salario = soma_salario / n
    media_filhos = total_filhos / n
    percentual_salario_ate_mil = (salario_ate_mil * 100) / n

    print('--- RESULTADOS ---')
    print(f'Media salarial: {media_salario:.2f}\nMedia de filhos: {media_filhos:.2f}\nPerc. pessoas com salario até R$1.0000,00: {percentual_salario_ate_mil:.2f} %')


main()
