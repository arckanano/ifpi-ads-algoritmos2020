# App calculo IR vigente e corrigida
def main():
    '''
                                Base de cálculo (R$)
    |-----------------------------------------------------------------------|
    | VIGENTE                   | CORRIGIDA                 | ALÍQUOTA (%)  |
    ------------------------------------------------------------------------|
    |até 1.903,98               | até 3.881,65              |   ISENTO      |
    |de 1.903,99 até 2.826,65   | de 3.881,66 até 5.714,11  |   7,5         |
    |de 2.826,66 até 3.751,05   | de 5.714,12 até 7.654,67  |   15          |
    |de 3.751,06 até 4.664,68   | de 7.654,68 até 9.564,42  |   22,5        |
    |acima de 4.664,68          | acima de 9.564,42         |   27,5        |
    |-----------------------------------------------------------------------|
    '''

    salario = float(input("Inserir salário: "))
    tabela_ir_vigente(salario)
    tabela_ir_corrigida(salario)

def tabela_ir_vigente(salario):
    # Valor maximo pago por cada faixa
    max_faixa_2 = (2826.65 - 1903.99) * 0.075
    max_faixa_3 = (3751.05 - 2826.66) * 0.15
    max_faixa_4 = (4664.68 - 3751.06) * 0.225

    ir_faixa_2 = (salario - 1903.98) * 0.075
    ir_faixa_3 = ((salario - 2826.66) * 0.15) + max_faixa_2
    ir_faixa_4 = ((salario - 3751.06) * 0.225) + max_faixa_3 + max_faixa_2
    ir_faixa_5 = ((salario - 4664.69) * 0.275) + max_faixa_4 + max_faixa_3 + max_faixa_2

    valor_a_pagar = 0

    if salario <= 1903.98:
        print('Isento')
    elif salario >= 1903.99 and salario <= 2826.65:
        print(f'Imposto a pagar pela tabela vigente: R${ir_faixa_2:.2f}')
    elif salario >= 2826.66 and salario <= 3751.05:
        print(f'Imposto a pagar pela tabela vigente: R${ir_faixa_3:.2f}')
    elif salario >= 3751.06 and salario <= 4664.68:
        print(f'Imposto a pagar pela tabela vigente: R${ir_faixa_4:.2f}')
    else:
        print(f'Imposto a pagar pela tabela vigente: R${ir_faixa_5:.2f}')


def tabela_ir_corrigida(salario):
    # Valor maximo pago por cada faixa
    max_faixa_2 = (5714.11 - 1903.99) * 0.075
    max_faixa_3 = (7654.67 - 5714.12) * 0.15
    max_faixa_4 = (9564.42 - 7654.68) * 0.225

    ir_faixa_2 = (salario - 1903.98) * 0.075
    ir_faixa_3 = ((salario - 5714.12) * 0.15) + max_faixa_2
    ir_faixa_4 = ((salario - 7654.68) * 0.225) + max_faixa_3 + max_faixa_2
    ir_faixa_5 = ((salario - 9564.42) * 0.275) + max_faixa_4 + max_faixa_3 + max_faixa_2

    valor_a_pagar = 0

    if salario <= 3881.65:
        print('Imposto a pagar pela tabela corrigida: Isento')
    elif salario >= 3881.66 and salario <= 5714.11:
        print(f'Imposto a pagar pela tabela corrigida : R${ir_faixa_2:.2f}')
    elif salario >= 5714.12 and salario <= 7654.67:
        print(f'Imposto a pagar pela tabela corrigida: R${ir_faixa_3:.2f}')
    elif salario >= 7654.68 and salario <= 9564.42:
        print(f'Imposto a pagar pela tabela corrigida: R${ir_faixa_4:.2f}')
    else:
        print(f'Imposto a pagar pela tabela corrigida: R${ir_faixa_5:.2f}')


main()
