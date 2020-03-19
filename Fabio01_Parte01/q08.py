# 8 - Leia 2 números, calcule e escreva a divisão da soma pela subtração dos números lidos.
#
# Entradas
num1 = int(input("Número 1: "))
num2 = int(input("Número 2: "))

# calculos
resultado = (num1 + num2) / (num1 - num2)

# resultado
print(f'Resposta: {resultado:.6f}')