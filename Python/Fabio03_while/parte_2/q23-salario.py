def main():

    qtd_funcionarios = int(input('Quantidade de funcionários: '))

    tot = 0
    valor_hora = 12
    valor_dependente = 40
    while tot < qtd_funcionarios:
        cod_funcionario = input('Cod. funcionário: ')
        horas_trabalhadas = int(input('Quantidade de horas trabalhadas: '))
        n_dependentes = int(input('Número de dependentes: '))
        
        valor_gerado = horas_trabalhadas * valor_hora # valor recebido pelas horas trabalhadas
        valor_recebido_dependente = n_dependentes * valor_dependente # valor recebido por cada dependente

        salario_bruto = valor_gerado + valor_recebido_dependente # valor recebido somando horas + dependentes
        
        
        salario_liquido = calculo_salario(salario_bruto, desconto_inss(salario_bruto), desconto_ir(salario_bruto))
        # salario_liquido = salario_bruto - desconto_inss(salario_bruto) - desconto_ir(salario_bruto)

        print('--- Valores ---')
        print(f'Desconto INSS: {desconto_inss(salario_bruto):.2f}')
        print(f'Desconto IR: {desconto_ir(salario_bruto):.2f}')
        print(f'Salário Líquido: {salario_liquido:.2f}')
        print('-'*20)

        tot += 1


def desconto_inss(salario):
    valor_desconto = salario * (8.5 / 100)
    return valor_desconto


def desconto_ir(salario):
    valor_desconto = salario * (5 / 100)
    return valor_desconto


def calculo_salario(salario, desc_inss, desc_ir):
    return salario - desc_inss - desc_ir


main()
