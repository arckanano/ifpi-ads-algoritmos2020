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
