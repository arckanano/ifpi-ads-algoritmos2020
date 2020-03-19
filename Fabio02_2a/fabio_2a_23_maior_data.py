def main():

    print("Insira a primeira data!")
    dia = int(input("Dia: "))
    mes = int(input("Mes: "))
    ano = int(input("Ano: "))

    print("Isira a segunda data!")
    dia2 = int(input("Dia: "))
    mes2 = int(input("Mes: "))
    ano2 = int(input("Ano: "))

    # Convertendo a data para dias
    # A data mais recente é aquela com maior número de dias

    saldo = (ano*365) + (mes*30) + dia
    saldo2 = (ano2 * 365) + (mes2 * 30) + dia2

    if saldo > saldo2:
        print("A primeira data a mais recente")
    else:
        print("A segunda data é mais recente")


main()
