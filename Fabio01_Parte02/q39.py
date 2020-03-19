# 39.  Leia três números inteiros e positivos (A, B, C) e calcule a seguinte expressão:

# Entradas
A = int(input('A: '))
B = int(input('B: '))
C = int(input('C: '))

# Processamento
R = (A + B) ** 2
S = (B + C) ** 2
D = (R + S) / 2

# Saída
print('Resultado: {}'.format(D))
