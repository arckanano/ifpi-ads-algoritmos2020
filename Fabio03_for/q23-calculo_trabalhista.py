def main():

    n = int(input('Número de funcionários: '))

    print('----- DADOS DO FUNCIONÁRIO -----')
    for i in range(1, n+1):
        codigo = int(input('Código do funcionários: '))
        numero_horas_trabalhadas = int(input('Número de horas trabalhadas: '))
        qtd_dependentes = int(input('Quantidade de dependentes: '))

        sal_bruto = salario_bruto(qtd_dependentes, numero_horas_trabalhadas)
        desconto_inss = inss(sal_bruto)
        desconto_ir = ir(sal_bruto)

        salario_liquido = sal_bruto - desconto_inss - desconto_ir

    print('')
    print(
        f'Salário Bruto: {sal_bruto}\nDesconto INSS: {desconto_inss}\nDesconto IR: {desconto_ir}\nSalário líquido: R${salario_liquido:.2f}')
    print('')


def salario_bruto(qtd_dependentes, numero_horas_trabalhadas):
    resultado = (numero_horas_trabalhadas * 12) + (qtd_dependentes * 40)
    return resultado


def inss(valor):
    resultado = valor * (8.5 / 100)
    return resultado


def ir(valor):
    resultado = valor * (5 / 100)
    return resultado


main()
