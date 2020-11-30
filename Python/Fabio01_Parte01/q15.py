# 15 - Leia o valor da base e altura de um triângulo, calcule e escreva sua área. (área=(base * altura)/2)
#
# Entradas
base = float(input("Tamanho da base: "))
altura = float(input("Tamanho da altura: "))

# calculo da área do triangulo
area = (base * altura) / 2

# resultado
print(f'Um triangulo de base {base} e altura {altura} tem area = {area}')