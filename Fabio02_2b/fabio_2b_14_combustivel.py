def main():

    tp_combustivel = input("Tipo de combustível:\n A - Alcool \n G - Gasolina \n =>").upper()
    qtd_combustivel = int(input("Quanto de combustível (litros): "))

    v_gasolina = 2.5
    v_alcool = 1.90

    if tp_combustivel == 'A' and qtd_combustivel <= 20:
        valor_pago = v_alcool * qtd_combustivel
        desconto = valor_pago * 3 / 100
        valor_c_desc = valor_pago - desconto
        print("Valor total: {}".format(valor_c_desc))
    elif tp_combustivel == 'A' and qtd_combustivel > 20:
        valor_pago = v_alcool * qtd_combustivel
        desconto = valor_pago * 5 / 100
        valor_c_desc = valor_pago - desconto
        print("Valor total: {}".format(valor_c_desc))
    elif tp_combustivel == 'G' and qtd_combustivel <= 20:
        valor_pago = v_gasolina * qtd_combustivel
        desconto = valor_pago * 4 / 100
        valor_c_desc = valor_pago - desconto
        print("Valor total: {}".format(valor_c_desc))
    elif tp_combustivel == 'G' and qtd_combustivel > 20:
        valor_pago = v_gasolina * qtd_combustivel
        desconto = valor_pago * 6 / 100
        valor_c_desc = valor_pago - desconto
        print("Valor total: {}".format(valor_c_desc))


main()
