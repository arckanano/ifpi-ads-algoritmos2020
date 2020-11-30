def main():
    '''
    Leia o turno em que um aluno estuda, sendo M para matutino, V para Vespertino ou N para Noturno e escreva a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso
    '''
    t = input("Turno: ").upper()

    if t == 'M':
        print("Bom dia")
    elif t == 'V':
        print("Boa tarde")
    elif t == 'N':
        print("Boa noite")
    else:
        print("Valor inválido!")
        print("Escolha: 'm' - matutino; 'v' - verpertino; 'n' - noturno")
        main()


main()
