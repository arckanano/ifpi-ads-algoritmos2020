def main():


    num1 = int(input("Numero 1: "))
    num2 = int(input("Numero 2: "))
    num3 = int(input("Numero 3: "))
    opcao = int(input("Qual opção: "))

    if opcao < 1 or opcao > 3:
        print("Opcão invalida!")
    elif opcao == 1:
        print(num1)
    elif opcao == 2:
        print(num2)
    elif opcao == 3:
        print(num3)

main()
