# Leia 2 (duas) frações (numerador e denominador), calcule e escreva a soma destas frações, escrevendo o 
# resultado em forma de fração.

# Entradas
numerador1 = int(input('Numerador 1: '))
denominador1 = int(input('Denominador 1: '))
numerador2 = int(input('Numerador 2: '))
denominador2 = int(input('Denominador 2: '))

# Processamento
denominadorComum = denominador1 * denominador2

numeradorX = ((denominadorComum / denominador1) * numerador1) + ((denominadorComum / denominador2) * numerador2)

# Saída
print('O resultado é {:.0f}/{}'.format(numeradorX, denominadorComum))
