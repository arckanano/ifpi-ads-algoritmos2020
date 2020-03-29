def main():

    v_h = float(input("Valor hora: "))
    h_m = float(input("Quantidade de horas trabalhadas: "))

    salario_bruto = salbruto(v_h, h_m)
    imposto_de_renda = calcir(salbruto(v_h, h_m))
    i_n_s_s = inss(salbruto(v_h, h_m))
    f_g_t_s = fgts(salbruto(v_h, h_m))
    total_descontos = totdesc(calcir(salbruto(v_h, h_m)),inss(salbruto(v_h, h_m)))
    salario_liquido = salliquido(salbruto(v_h, h_m), calcir(salbruto(v_h, h_m)), fgts(salbruto(v_h, h_m)))

    print(f"Salário Bruto: {salario_bruto}")
    print(f"(-)IR: {imposto_de_renda}")
    print(f"(-)INSS: {i_n_s_s}")
    print(f"FGTS (11%): {f_g_t_s}")
    print(f"Total de descontos: {total_descontos}")
    print(f"Salário Liquido: {salario_liquido}")


def salbruto(a, b):
    return a * b


def calcir(salario):
    if salario > 2500:
        return 2500 * 20 / 100
    elif 1500 > salario <= 2500:
        return salario * 10 / 100
    elif 900 > salario <= 1500:
        return salario * 5 / 100
    elif salario <= 900:
        return 0


def inss(salario):
    return salario * 10/100


def fgts(salario):
    return salario * 11/100


def totdesc(ir, inss):
    return ir + inss


def salliquido(salario, irr, ins):
    return salario - irr - ins


main()
