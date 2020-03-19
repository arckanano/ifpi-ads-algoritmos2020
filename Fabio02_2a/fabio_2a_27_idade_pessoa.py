def main():

    print("Insira a primeira data!")
    dia = int(input("Dia nascimento: "))
    mes = int(input("Mes nascimento: "))
    ano = int(input("Ano nascimento: "))

    print("Isira a segunda data!")
    dia2 = int(input("Dia atual: "))
    mes2 = int(input("Mes atual: "))
    ano2 = int(input("Ano atual: "))

    # Convertendo a data para dias

    saldo = (ano*365) + (mes*30) + dia
    saldo2 = (ano2 * 365) + (mes2 * 30) + dia2

    # calculando a diferença de dias

    diferenca = saldo2 - saldo

    # Determinando a idade

    anoPessoa = diferenca // 365
    s = diferenca % 365

    mesPessoa = s // 30
    diaPessoa = s % 30

    # Resultados
    print("A pessoa possui {} ano(s) {} mes(es) e {} dia(s)".format(anoPessoa, mesPessoa, diaPessoa))


main()
