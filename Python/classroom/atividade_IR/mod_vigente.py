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
