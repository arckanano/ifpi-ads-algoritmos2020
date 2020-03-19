# 1 - Leia uma velocidade em m/s, calcule e escreva esta velocidade em km/h. (Vkm/h = Vm/s * 3.6)
#
# entradas
velocidade_metro_segundo = float(input("Velocidade em m/s: "))
# conversor de velocidade
metro_segundo_para_kilometro_hora = velocidade_metro_segundo * 3.6
# resultado
print(f'{velocidade_metro_segundo} m/s em km/h = {metro_segundo_para_kilometro_hora} km/h ')