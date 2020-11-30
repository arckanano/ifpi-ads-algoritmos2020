# 25.  Leia um número inteiro de metros, calcule e escreva quantos Km e quantos metros ele corresponde.

# Entrada
qtd_metros = int(input('quantidade de metros: '))

# Processamento
valor_km = qtd_metros // 1000
valor_metro = qtd_metros % 1000

# Saída
print('{} metros equivale a {} km e {} metros.'.format(qtd_metros, valor_km, valor_metro))
