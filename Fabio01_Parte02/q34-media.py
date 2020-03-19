# Leia 3 números, calcule e escreva a média dos números.

# entrada
numero = int(input('Numero: '))

# processamento
centena = numero // 100
resto = numero % 100

dezena = resto // 10
unidade = resto % 10

media = (centena+dezena+unidade) / 3

# saida
print(media)
