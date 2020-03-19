def main():

    opcao = int(input("Qual opção: "))
    num1 = 1
    num2 = 2
    num3 = 3

    if opcao < 1 or opcao > 3:
        print("Opcão invalida! Tente novamente!")
        return main()
    elif opcao == 1:
        print(num1)
    elif opcao == 2:
        print(num2)
    elif opcao == 3:
        print(num3)

main()
