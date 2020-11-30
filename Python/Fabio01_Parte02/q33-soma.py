# 33.  Leia um número inteiro (3 dígitos), calcule e escreva a soma do número com seu inverso.

# entrada
numero = int(input('Numero: '))

# processamento
centena = numero // 100
resto = numero % 100

dezena = resto // 10
unidade = resto % 10

# Novo numero
nova_centena = unidade * 100
nova_dezena = dezena * 10
nova_unidade = centena

# saida
print(numero+(nova_centena+nova_dezena+nova_unidade))
