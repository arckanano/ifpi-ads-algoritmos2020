# Leia um número inteiro de horas, calcule e escreva quantas semanas, quantos dias e quantas horas ele
# corresponde.

# entrada
numero = int(input('numero: '))

# processamento
qtdSemana = numero // 168
restoSemana = numero % 168

qtdDias = restoSemana // 24
qtdHoras =  restoSemana % 24

print('{} semana(s), {} dia(s), {} hora(s)'.format(qtdSemana, qtdDias, qtdHoras))
