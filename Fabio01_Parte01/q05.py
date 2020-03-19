# 5 - Leia um número inteiro (3 dígitos), calcule e escreva a soma de seus elementos (C + D + U).
#
# Entrada de numero de 3 digitos
numero = int(input("Número: "))

# Quebrar o número em unidade, dezenas e centenas
centena = numero // 100
dezenas = (numero % 100) // 10
unidade = (numero % 100) % 10

# resultado
print(f'{centena} centenas, {dezenas} dezenas e {unidade} unidades')