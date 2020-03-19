# 6 - Leia uma velocidade em km/h, calcule e escreva esta velocidade em m/s. (Vm/s = Vkm/h / 3.6)

# entrada
vel_kmph = int(input("Velocidade em km/h: "))

# conversor
kpmh_to_ms = vel_kmph / 3.6

# resultado
print(f'{vel_kmph} km/h = {kpmh_to_ms:.2f} m/s')