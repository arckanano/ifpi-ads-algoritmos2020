# 9 - Leia 2 números (A, B) e escreva-os em ordem inversa (B, A).
#
# Entradas
A = int(input("Número 1: "))
B = int(input("Número 2: "))

# Troca de valores
A, B = B, A

# resultados
print(f'A = {A} | B = {B}')