def main():
    menu = print(''''
                Ate 5Kg     Acima de 5Kg
    1 - File    R$4.90      R$5.80
    2 - Alcatra R$5.90      R$6.80
    3 - Picanha R$6,90      R$7.80
    ''')
    tipo_de_carne = int(input("Qual carne: ")).upper()
    quantidade_de_carne = float(input("Quantidade de carne: "))
    modo_de_pagamento = str(input("Pagar no cartao? (S/N): ")).upper()
    
    if tipo_de_carne == 1:
        if quantidade_de_carne <= 5:
            total_da_compra = quantidade_de_carne * 4.90
        else:
            total_da_compra = quantidade_de_carne * 5.80
    elif tipo_de_carne == 2:
        if quantidade_de_carne <= 5:
            total_da_compra = quantidade_de_carne * 5.90
        else:
            total_da_compra = quantidade_de_carne * 6.80    
    elif tipo_de_carne == 3:
        if quantidade_de_carne <= 5:
            total_da_compra = quantidade_de_carne * 6.90
        else:
            total_da_compra = quantidade_de_carne * 7.80

# Cupom
    if tipo_de_carne == 1:
        print(f"Tipo de carne:          {tipo_de_carne}")
        print(f"Quantidade de carne:    {quantidade_de_carne}")
        print(f"Preco total:            {}")
        if modo_de_pagamento == "S":
            print("Tipo de pagamento:  Cartão")
        else:
            print("Tipo de pagamento:   Dinheiro")
        print(f"Valor do desconto:      {}")
        print(f"Valor a pagar:          {}")

def calculo_desconto(valor):
    return valor * (5/100)

main()