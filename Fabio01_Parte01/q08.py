# 8 - Leia 2 números, calcule e escreva a divisão da soma pela subtração dos números lidos.
#

def main():
    num1 = int(input("Número 1: "))
    num2 = int(input("Número 2: "))

    resultado = divide2(soma2(num1, num2), subtrai2(num1, num2))
    print(f'Resposta: {resultado}')

def soma2(a,b):
    return a + b

def subtrai2(a,b):
    return a - b

def divide2(a,b):
    return a / b


main()