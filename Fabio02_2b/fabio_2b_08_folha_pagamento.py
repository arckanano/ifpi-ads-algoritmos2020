def main():

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

    v_h = float(input("Valor hora: "))
    h_m = float(input("Quantidade de horas trabalhadas: "))

    print("Salário Bruto: {}".format(salbruto(v_h, h_m)))
    print("(-)IR: {}".format(calcir(salbruto(v_h, h_m))))
    print("(-)INSS: {}".format(inss(salbruto(v_h, h_m))))
    print("FGTS (11%): {}".format(fgts(salbruto(v_h, h_m))))
    print("Total de descontos: {}".format(totdesc(calcir(salbruto(v_h, h_m)),inss(salbruto(v_h, h_m)))))
    print("Salário Liquido: {}".format(salliquido(salbruto(v_h, h_m), calcir(salbruto(v_h, h_m)), fgts(salbruto(v_h, h_m)))))


main()
