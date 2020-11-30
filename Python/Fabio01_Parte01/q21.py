# 21 - Leia uma temperatura em °F, calcule e escreva a equivalente em °C. (t°C = (5 * t°F - 160) / 9).
#
# Entradas
farenheigh = float(input("Temperatura: "))

# calculo
celsius = (5 * farenheigh - 160) / 9

# resultado
print(f'{farenheigh} farenheigh = {celsius} celsius')