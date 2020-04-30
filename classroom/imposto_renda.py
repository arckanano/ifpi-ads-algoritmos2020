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

    # Valor maximo pago por cada faixa
    max_faixa_2 = (2826.65 - 1903.99) * 0.075
    max_faixa_3 = (3751.05 - 2826.66) * 0.15
    max_faixa_4 = (4664.68 - 3751.06) * 0.225
    # max_faixa_4 = (salario - 4664.69) * 0.275


    ir_faixa_2 = (salario - 1903.98) * 0.075
    ir_faixa_3 = ((salario - 2826.66) * 0.15) + max_faixa_2
    ir_faixa_4 = ((salario - 3751.06) * 0.225) + max_faixa_3 + max_faixa_2
    ir_faixa_5 = ((salario - 4664.69) * 0.275) + max_faixa_4 + max_faixa_3 + max_faixa_2
    
    print('faixa 2', ir_faixa_2)
    print('faixa 3', ir_faixa_3)
    print('faixa 4', ir_faixa_4)
    print('faixa 4', ir_faixa_5)
    
    # tabela_ir_vigente(salario, ir_faixa_2, ir_faixa_3, ir_faixa_4)

def tabela_ir_vigente(salario, ir_faixa_2, ir_faixa_3, ir_faixa_4):
    valor_a_pagar = 0
    if salario <= 1903.98:
        print('Isento')
    elif salario >= 1903.99 and salario <= 2826.65:
        valor_a_pagar = ir_faixa_1
        print(f'Valor a pagar de ir R${valor_a_pagar:.2f}')
    elif salario >= 2826.66 and salario <= 3751.05:
        valor_a_pagar = ir_faixa_1 + ir_faixa_2
        print(f'Valor a pagar de ir R${valor_a_pagar:.2f}')
    elif salario >= 3751.06 and salario <= 4664.68:
        valor_a_pagar = ir_faixa_1 + ir_faixa_2 + ir_faixa_3
        print(f'Valor a pagar de ir R${valor_a_pagar:.2f}')
    else:
        valor_a_pagar = ir_faixa_1 + ir_faixa_2 + ir_faixa_3 + ir_faixa_4
        print(f'Valor a pagar de ir R${valor_a_pagar:.2f}')

main()