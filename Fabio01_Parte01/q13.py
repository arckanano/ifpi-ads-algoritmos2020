# 13 - Leia um valor em real (R$), calcule e escreva 70% deste valor.
#
# Entrada
valor = float(input("Valor em Real(R$): "))

# percentual
percentual = ((valor / 100) * 70)

# resultado
print(f' 70% de {valor} = {percentual:.2f}')