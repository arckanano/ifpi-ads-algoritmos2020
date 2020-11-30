import functions
# 7 - Leia 3 números, calcule e escreva a soma dos 2 primeiros e a diferença entre os 2 últimos.

# Entradas
def main():
    num1 = int(input("Número 1: "))
    num2 = int(input("Número 2: "))
    num3 = int(input("Número 3: "))
    
    soma_2_primeiros = functions.soma2(num1, num2)
    diferenca_2_ultimos = functions.subtrai2(num2, num3)

    print(f'Soma dos 2 primeiros: {soma_2_primeiros} \nDiferença 2 ultimos = {diferenca_2_ultimos}')


main()