'''

'''
def main():

    # Inserir data atual em números
    diaAtual = int(input("Dia atual: "))
    mesAtual = int(input("Mes atual: "))
    anoAtual = int(input("Ano atual: "))

    diaNasc = int(input("Dia nascimento: "))
    mesNasc = int(input("Mes nascimento: "))
    anoNasc = int(input("Ano nascimento: "))

    # Transformando tudo em dias
    # considerando ano de 365 dias, mes de 30 dias
    diasAteNascimento = (anoNasc*365) + ((mesNasc - 1) * 30) + diaNasc
    diasAteHoje = (anoAtual*365) + ((mesAtual - 1) * 30) + diaAtual

    diferença = diasAteHoje - diasAteNascimento

    # Calculo da idade

    idadeAno = diferença // 365

    print("Voce tem {} anos".format(idadeAno))


main()
