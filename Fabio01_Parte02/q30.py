# Leia um número inteiro de minutos, calcule e escreva quantos dias, quantas horas e quantos minutos ele
# corresponde.

# Entrada
minutos = int(input('Quantos minutos: '))

# processamento
qtdDia = minutos // 1440
resto = minutos % 1440

qtdHora = resto // 60
qtdMinuto = resto % 60

# Saida
print('{} dias {} horas e {} minutos'.format(qtdDia, qtdHora, qtdMinuto))
