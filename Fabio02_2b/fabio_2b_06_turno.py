def main():

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
