# Conta cédulas

# Entrada

valor_saque = int(input('Valor do saque: '))

# processamento

nota50 = valor_saque // 50
resto = valor_saque % 50

nota10 = resto // 10
resto10 = resto % 10

nota5 = resto10 // 5
nota1 = resto10 % 5

# Saída
print('{} notas de R$50 \n' '{} notas de R$10 \n' '{} notas de R$5 \n' '{} notas de R$1'.format(nota50, nota10, nota5, nota1))
