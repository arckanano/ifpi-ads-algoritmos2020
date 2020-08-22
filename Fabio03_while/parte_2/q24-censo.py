def main():

    dado = int(input('Quantidade de dados: '))

    tot = 0
    soma_salario = 0
    soma_filho = 0
    salario_ate_mil = 0
    while tot < dado:
        salario = float(input('Salário: '))
        qtd_filhos = int(input('Quantidade de filhos: '))

        if salario <= 1000:
            salario_ate_mil += 1
        soma_salario += salario
        soma_filho += qtd_filhos

        tot += 1

    media_salario = calc_media(soma_salario, dado)
    media_filhos = calc_media(soma_filho, dado)
    perc_salario_ate_mil = (salario_ate_mil * 100) / dado

    print('--- Resultados ---')
    print(f'Média de salário da população: R${media_salario:.2f}')
    print(f'Média de filhos da população: {media_filhos}')
    print(f'Percentual de pessoas com salário até R$1000,00: {perc_salario_ate_mil:.2f}%')


def calc_media(soma, qtd):
    media = soma / qtd
    return media


main()
