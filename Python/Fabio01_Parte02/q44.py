# Sabendo que latão é constituído de 70% de cobre e 30% de zinco, escreva um algoritmo que calcule a
# quantidade de cada um desses componentes para se obter certa quantidade de latão (em kg), informada
# pelo usuário.

# Entrada
quantia_latao = float(input('Quanto quilos de latão: '))

# Processamento
cobre = quantia_latao * (70/100)
zinco = quantia_latao * (30/100)

# Saída
print('Seu latão é feito de {}Kg de Cobre e {}Kg de Zinco'.format(cobre,zinco))
