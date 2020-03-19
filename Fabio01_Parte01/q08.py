import functions
# 8 - Leia 2 números, calcule e escreva a divisão da soma pela subtração dos números lidos.
#

def main():
    num1 = int(input("Número 1: "))
    num2 = int(input("Número 2: "))

    resultado = divide2(functions.soma2(num1, num2), functions.subtrai2(num1, num2))
    print(f'Resposta: {resultado}')


main()