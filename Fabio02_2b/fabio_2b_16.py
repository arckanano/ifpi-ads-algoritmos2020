def main():
    menu = print(''''
                Ate 5Kg     Acima de 5Kg
    1 - file    R$4.90      R$5.80
    2 - alcatra R$5.90      R$6.80
    3 - picanha R$6,90      R$7.80
    ''')
    tipo_de_carne = int(input("Qual carne: "))
    quantidade_de_carne = float(input("Quantidade de carne: "))
    modo_de_pagamento = str(input("Pagar no cartao? (s/n): "))
    
    total_da_compra = 0.0
    if tipo_de_carne == 1:
        carne = 'File'
        if quantidade_de_carne <= 5:
            total_da_compra = quantidade_de_carne * 4.90
        else:
            total_da_compra = quantidade_de_carne * 5.80
    elif tipo_de_carne == 2:
        carne = 'Alcatra'
        if quantidade_de_carne <= 5:
            total_da_compra = quantidade_de_carne * 5.90
        else:
            total_da_compra = quantidade_de_carne * 6.80    
    elif tipo_de_carne == 3:
        carne = 'Picanha'
        if quantidade_de_carne <= 5:
            total_da_compra = quantidade_de_carne * 6.90
        else:
            total_da_compra = quantidade_de_carne * 7.80

    desconto = 0.0
    meio_de_pagamento = 'Dinheiro'
    if modo_de_pagamento == 's':
        meio_de_pagamento = 'Cartão'
        desconto = total_da_compra * 0.05

    valor_total_da_compra = total_da_compra - desconto

    print("\n--- CUPOM FISCAL ---")
    print(f'Tipo de carne: {carne}')
    print(f'Quantidade_de_carne: {quantidade_de_carne} Kg')
    print(f'Modo de pagamento: {meio_de_pagamento}')
    print(f'Valor da compra (s/desc): {total_da_compra:.2f}')
    print(f'Desconto = {desconto:.2f}')
    print('#####################')
    print(f'Valor Total: {valor_total_da_compra:.2f}')


main()