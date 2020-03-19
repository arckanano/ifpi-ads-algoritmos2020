# 3 - Leia um valor em minutos, calcule e escreva o equivalente em horas e minutos.
#
# Entrada dos minutos
minutos = int(input("Minutos: "))

# Descobrir quantas horas
horas = minutos // 60

# Descobrir minutos
minutos_restantes = minutos % 60

# Resultados
print(f'{minutos} = {horas} horas e {minutos_restantes} minutos')
