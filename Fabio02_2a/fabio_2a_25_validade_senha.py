def main():

    login = input("Login: ")
    senha = int(input("Input: "))

    if senha == 1234:
        print("Olá %s" % login)
        print("Acesso permitido!")
    else:
        print("Acesso negado!")
        print("Login ou senha estão incorretos.")


main()
