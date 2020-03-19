# 2 - Leia um valor em horas e um valor em minutos, calcule e escreva o equivalente em minutos.

# entrada das horas e minutos
horas = int(input("Horas: "))
minutos = int(input("Minutos: "))

# conversor para minutos
total_minutos = (horas * 60) + minutos

# resultado
print(f'{horas} horas e {minutos} minutos = {total_minutos} minutos')