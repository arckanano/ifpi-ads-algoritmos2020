# 27.  Leia  um  número  inteiro  de  segundos,  calcule  e  escreva  quantas  horas,  quantos  minutos  e  quantos
# segundos ele corresponde.

# Entrada de dados
qtd_segundos = int(input('Quantos segundos: '))

# Processamento
valorHoras = qtd_segundos // 3600
valorMinutos = (qtd_segundos % 3600) // 60
#valorSegundos = ((qtd_segundos % 3600) // 60) // 60
valorSegundos = (qtd_segundos % 3600) % 60

# Saida

print('{} horas {} minutos {} segundos.'.format(valorHoras, valorMinutos, valorSegundos))
