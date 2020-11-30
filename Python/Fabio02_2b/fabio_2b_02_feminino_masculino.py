def main():
'''
Leia uma letra, verifique se letra é "F" ou "M" e escreva F - Feminino, M - Masculino, Sexo Inválido
'''
    print("Digite 'F' para Feminino e 'M' para Masculino")
    l = input("Letra: ").upper()

    if l == "F":
        print("Feminino")
    elif l == "M":
        print("Masculino")
    else:
        print("Letra inválida")


main()
