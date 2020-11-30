# 22 - Leia um valor em km, calcule e escreva o equivalente em m.
#
# Entrada
valor_em_kilometro = float(input("Valor em kilometros: "))

# calculo
valor_em_metros = valor_em_kilometro * 1000

# resultado
print(f"{valor_em_kilometro:.2f} Km = {valor_em_metros:.2f} m")