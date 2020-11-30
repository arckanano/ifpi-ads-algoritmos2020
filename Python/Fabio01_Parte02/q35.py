# 35.  Leia  um  número  inteiro  (4  dígitos),  calcule  e  escreva a  soma  dos  elementos  que  o  compõem.

# Entradas
num = int(input('Número binario: '))

# Processamento
# Separação das unidades

milhar = num // 1000
restoMilhar = num % 1000

centena = restoMilhar // 100
restoCentena = restoMilhar % 100

dezena = restoCentena // 10
unidade = restoCentena % 10

soma = milhar+centena+dezena+unidade

# Saida
print(soma)
