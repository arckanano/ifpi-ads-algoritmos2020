def main():

    sal = float(input("Salário funcionário: "))

    if sal >= 1500:
        aumento = sal / 100 * 5
        nsal = sal+aumento
        print("Salário: %0.2f" % sal)
        print("aumento de 5%")
        print("Aumento: %0.2f " % aumento)
        print("Novo salário: %0.2f " % nsal)

    elif sal > 700 and sal < 1500:
        aumento = sal / 100 * 10
        nsal = sal+aumento
        print("Salário: %0.2f" % sal)
        print("aumento de 10%")
        print("Aumento: %0.2f " % aumento)
        print("Novo salário: %0.2f " % nsal)

    elif sal > 280 and sal <= 700:
        aumento = sal / 100 * 15
        nsal = sal+aumento
        print("Salário: %0.2f" % sal)
        print("aumento de 15%")
        print("Aumento: %0.2f " % aumento)
        print("Novo salário: %0.2f " % nsal)
        
    elif sal <= 280:
        aumento = sal / 100 * 20
        nsal = sal+aumento
        print("Salário: %0.2f" % sal)
        print("aumento de 20%")
        print("Aumento: %0.2f " % aumento)
        print("Novo salário: %0.2f " % nsal)


main()
