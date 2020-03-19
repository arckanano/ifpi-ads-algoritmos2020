# 7 - Leia 3 números, calcule e escreva a soma dos 2 primeiros e a diferença entre os 2 últimos.

# Entradas
num1 = int(input("Número 1: "))
num2 = int(input("Número 2: "))
num3 = int(input("Número 3: "))

# cálculos
soma = num1 + num2
diferenca = num2 - num3

# resultado
print(f'Soma de {num1} + {num2} = {soma}')
print(f'Diferença de {num2} e {num3} = {diferenca}')