def main():

    nota1 = float(input("Nota 1 aluno: "))
    nota2 = float(input("Nota 2 aluno: "))

    media = (nota1 + nota2) / 2

    if media >= 7:
        print("Aprovado")
    elif media > 5 and media < 7:
        print("Prova final")
    elif media < 5:
        print("Reprovado")


main()
