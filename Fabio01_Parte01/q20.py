# 20 - Leia uma temperatura em °C, calcule e escreva a equivalente em °F. (t°F = (9 * t°C + 160) / 5)
#
# Entradas
celsius = float(input("Temperatura em Celcius: "))

# Calculo
farenheigh = (9 * celsius + 160) / 5

# resultado
print(f'{celsius} celsius = {farenheigh} farenheigh')