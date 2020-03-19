# 37.  Leia a idade de uma pessoa expressa em dias e escreva-a expressa em anos, meses e dias.

# Entradas
idadeEmDias = int(input('Quantos dias: '))

# Processamento

totalAnos = idadeEmDias // 365
resto = idadeEmDias % 365

totalMeses = resto // 30
totalDias = resto % 30

# Saída
print('{} anos, {} meses e {} dias'.format(totalAnos, totalMeses, totalDias))
