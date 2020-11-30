# 14 - Leia 3 notas de um aluno e o peso de cada nota, calcule e escreva a média ponderada.
#
# Notas e pesos
nota_1 = float(input("Nota 1: "))
nota_2 = float(input("Nota 2: "))
nota_3 = float(input("Nota 3: "))
peso_nota_1 = int(input("Peso nota 1: "))
peso_nota_2 = int(input("Peso nota 2: "))
peso_nota_3 = int(input("Peso nota 3: "))

# calculo da media ponderada
media_ponderada = ((nota_1 * peso_nota_1) + (nota_2 * peso_nota_2) + (nota_3 * peso_nota_3)) / (peso_nota_1 + peso_nota_2 + peso_nota_3)

# resultado
print(f'Média: {media_ponderada:.2f}')