import functions
# 10 - Leia 2 números inteiros, calcule e escreva o quociente e o resto da divisão do 1o pelo 2o.
#
# Entradas
def main():
    numero1 = int(input("Numero 1 = "))
    numero2 = int(input("Número 2 = "))

    # Calculos
    # quociente = functions.divide2(numero1, numero2)
    # resto_da_divisao = functions.resto_da_divisao(numero1, numero2)

    # resultados
    print(f'Quociente = {functions.divide2(numero1, numero2)}\nResto = {functions.resto_da_divisao(numero1, numero2)}')

main()