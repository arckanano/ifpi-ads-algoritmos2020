# Parcelamento

# Entrada
valProd = int(input('Valor do produto: '))

# Processamento
entrada = (valProd // 3) + (valProd % 3)
parcelas = (valProd - entrada) / 2

# saida
print('''
>>>>>>>>PARCELAMENTO<<<<<<<<
|   Entrada     |   R${:.2f}|
|   Parcela 1   |   R${:.2f}|
|   Parcela 2   |   R${:.2f}|
'''.format(entrada, parcelas, parcelas))
