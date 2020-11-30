def main():

    salario = float(input("Salário funcionário: "))

    if salario >= 1500:
        aumento = valor_aumento(salario, 5)
        novo_salario = salario + aumento
        print("Salário: %0.2f" % salario)
        print("aumento de 5%")
        print("Aumento: %0.2f " % aumento)
        print("Novo salário: %0.2f " % novo_salario)

    elif salario > 700 and salario < 1500:
        aumento = valor_aumento(salario, 10)
        novo_salario = salario + aumento
        print("Salário: %0.2f" % salario)
        print("aumento de 10%")
        print("Aumento: %0.2f " % aumento)
        print("Novo salário: %0.2f " % novo_salario)

    elif salario > 280 and salario <= 700:
        aumento = valor_aumento(salario, 15)
        novo_salario = salario + aumento
        print("Salário: %0.2f" % salario)
        print("aumento de 15%")
        print("Aumento: %0.2f " % aumento)
        print("Novo salário: %0.2f " % novo_salario)
        
    elif salario <= 280:
        # aumento = salario / 100 * 20
        aumento = valor_aumento(salario, 20)
        novo_salario = salario + aumento
        print("Salário: %0.2f" % salario)
        print("aumento de 20%")
        print("Aumento: %0.2f " % aumento)
        print("Novo salário: %0.2f " % novo_salario)
    
def valor_aumento(salario, porc):
    aumento = salario / 100 * porc
    return aumento


main()
