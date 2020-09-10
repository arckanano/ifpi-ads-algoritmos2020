def main():

    senha = input('Senha: ')
    conferir(senha)


def conferir(senha):
    tudo_ok = 0
    o_que_falta = ''
    if len(senha) < 6:
        print(f'A senha deve possuir pelo menos 6 dígitos!')
        # return False
    else:
        # Significa que a senha tem pelo menos 6 letras, e isso já conta como uma exigência.
        tudo_ok += 1
        # print(6 - len(senha))
        if has_number(senha) == True:
            tudo_ok += 1
        else:
            o_que_falta += 'número '
        if has_lower(senha) == True:
            tudo_ok += 1
        else:
            o_que_falta += 'letra minúscula '
        if has_upper(senha) == True:
            tudo_ok += 1
        else:
            o_que_falta += 'letra maiúscula '
        if has_special(senha) == True:
            tudo_ok += 1
        else:
            o_que_falta += 'caractere especial '
        if tudo_ok < 5:
            print(f'Falta {5 - tudo_ok} item(s) >>> ' + o_que_falta)


def has_number(senha):
    numbers = '1234567890'
    for i in range(len(senha)):
        tot = 0
        if senha[i] in numbers:
            tot += 1
            if tot >= 1:
                return True

    return False


def has_lower(senha):
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    for i in range(len(senha)):
        tot = 0
        if senha[i] in lower_case:
            tot += 1
            if tot >= 1:
                return True

    return False


def has_upper(senha):
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(senha)):
        tot = 0
        if senha[i] in upper_case:
            tot += 1
            if tot >= 1:
                return True

    return False


def has_special(senha):
    special_characters = "!@#$%^&*()-+"
    for i in range(len(senha)):
        tot = 0
        if senha[i] in special_characters:
            tot += 1
            if tot >= 1:
                return True

    return False


main()
