def main():

    v_gasolina = 2.5
    v_alcool = 1.90

    tp_combustivel = input("Tipo de combustível:\n A - Alcool \n G - Gasolina \n =>").upper()
    qtd_combustivel = int(input("Quanto de combustível (litros): "))


    if tp_combustivel == 'A' and qtd_combustivel <= 20:
        valor_c_desc = alcool_ate_20_l(v_alcool, qtd_combustivel, 3)
        print(f"Valor total: {valor_c_desc:.3f}")
    elif tp_combustivel == 'A' and qtd_combustivel > 20:
        valor_c_desc = alcool_acima_20_l(v_alcool, qtd_combustivel, 5)
        print(f"Valor total: {valor_c_desc:.3f}")
    elif tp_combustivel == 'G' and qtd_combustivel <= 20:
        valor_c_desc = gasolina_ate_20_l(v_gasolina, qtd_combustivel, 4)
        print(f"Valor total: {valor_c_desc:.3f}")
    elif tp_combustivel == 'G' and qtd_combustivel > 20:
        valor_c_desc = gasolina_acima_20_l(v_gasolina, qtd_combustivel, 6)
        print(f"Valor total: {valor_c_desc:.3f}")

def alcool_ate_20_l(valor_combustivel, qtd_combustivel, perc_desc):
    return (valor_combustivel * qtd_combustivel) - ((valor_combustivel * qtd_combustivel) * (perc_desc / 100))

def alcool_acima_20_l(valor_combustivel, qtd_combustivel, perc_desc):
    return (valor_combustivel * qtd_combustivel) - ((valor_combustivel * qtd_combustivel) * (perc_desc / 100))

def gasolina_ate_20_l(valor_combustivel, qtd_combustivel, perc_desc):
    return (valor_combustivel * qtd_combustivel) - ((valor_combustivel * qtd_combustivel) * (perc_desc / 100))

def gasolina_acima_20_l(valor_combustivel, qtd_combustivel, perc_desc):
    return (valor_combustivel * qtd_combustivel) - ((valor_combustivel * qtd_combustivel) * (perc_desc / 100))


main()
