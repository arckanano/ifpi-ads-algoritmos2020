# Leia a idade de uma pessoa expressa em anos, meses e dias e escreva-a expressa apenas em dias

# Entrada
idadeAnos = int(input('Quantos anos: '))
idadeMeses = int(input('Quantos meses: '))
idadeDias = int(input('Quantos dias: '))

# Processamento
totalEmDias = (idadeAnos * 365) + (idadeMeses * 30) + (idadeDias)

# Saída
print('Total em dias: %d' % (totalEmDias))
