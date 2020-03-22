def main():
    '''
    Verifique a validade de uma senha fornecida pelo usuário. A senha é 1234. O algoritmo deve escrever uma mensagem de permissão de acesso ou não.
    '''
    login = input("Login: ")
    senha = int(input("Input: "))

    if senha == 1234:
        print("Olá %s" % login)
        print("Acesso permitido!")
    else:
        print("Acesso negado!")
        print("Login ou senha estão incorretos.")


main()
