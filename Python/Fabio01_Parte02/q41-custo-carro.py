# O  custo  ao  consumidor  de  um  carro  novo  é  a  soma  do  custo  de  fábrica  com  a  percentagem  do
# distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que a percentagem do distribuidor
# seja de 28% e os impostos de 45%, escreva um algoritmo que leia o custo de fábrica de um carro e
# escreva o custo ao consumidor

# Entradas
custo_fabrica = float(input('Valor do carro na fabrica: '))
perc_distribuidor = custo_fabrica * (28/100)
impostos = custo_fabrica * (45/100)

# Processamento
custo_carro = custo_fabrica + perc_distribuidor     + impostos

# Saida
print('O valor final do carro é: %.2f' % (custo_carro))
