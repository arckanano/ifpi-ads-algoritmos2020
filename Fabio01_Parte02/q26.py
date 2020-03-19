# 26.  Leia um número inteiro de dias, calcule e escreva quantas semanas e quantos dias ele corresponde.

# Entrada
qtd_dias = int(input('quantidade de dias: '))

# processamento
valor_semanas = qtd_dias // 7
valor_dias = qtd_dias % 7

# saida
print('{} de dias equivale a {} semana(s) e {} dia(s).'.format(qtd_dias, valor_semanas, valor_dias))
