def main():

    # tamnhado_da_senha = int(input(''))
    texto = '#Hacker1'
    resultado = verificar_tamanho(texto)
    print(resultado)


def verificar_tamanho(senha):
    if len(senha) < 6:
        return (f'Faltam {6 - len(senha)} caracteres!!!')
    else:
        confere(senha)


def confere(senha):
    tot = 0
    if has_number:
        tot += 1
    return tot

def has_number(senha):
    numbers = "0123456789"
    for i in range(len(senha)):
        if senha[i] in numbers == True:
            return 0
        else:
            return 1


# def has_lower(senha):
#     lower_case = "abcdefghijklmnopqrstuvwxyz"
#     for i in range(len(senha)):
#         if senha[i] in lower_case:
#             return True


# def has_upper(senha):
#     upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     for i in range(len(senha)):
#         if senha[i] in upper_case:
#             return True


# def has_special(senha):
#     special_characters = "!@#$%^&*()-+"
#     for i in range(len(senha)):
#         if senha[i] in special_characters:
#             return True


main()
