from datetime import datetime

def main():

    # Inserir data atual em números
    hoje = datetime.now()
    diaAtual = hoje.day
    mesAtual = hoje.month
    anoAtual = hoje.year

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
    # resto = diferença % 365

    # idadeMes = resto // 30
    # idadeDias = idadeMes % 30

    print("Voce tem {} anos".format(idadeAno))
    # print("Voce tem {} anos, {} meses e {} dias de vida".format(idadeAno, idadeMes, idadeDias))


main()
