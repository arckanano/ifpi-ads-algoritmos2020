def main():

    dia = int(input("dia: "))
    mes = int(input("mes: "))
    ano = int(input("ano: "))

    if dia < 1 or dia > 30:
        print("Data invalida")
    elif mes < 1 or mes > 12:
        print("Data invalida")
    else:
        print("{} do {} de {}".format(dia, mes, ano))

main()
