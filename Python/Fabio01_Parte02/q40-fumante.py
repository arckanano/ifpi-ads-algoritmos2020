# Calcule a quantidade de dinheiro gasta por um fumante. Dados de entrada: o número de anos que ele 
# fuma, o nº de cigarros fumados por dia e o preço de uma carteira (1 carteira tem 20 cigarros)

# Entradas
anosFumando = int(input('Anos Fumando: '))
cigarrosDias = int(input('Cigarro por dia: '))
valorCarteira = int(input('Valor da carteira: '))

# processamento
dinheiroGasto = ((cigarrosDias * (anosFumando * 365)) / 20) * valorCarteira

# Saída
print('Dinheiro gasto: R${}'.format(dinheiroGasto))
