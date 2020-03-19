# 6 - Leia uma velocidade em km/h, calcule e escreva esta velocidade em m/s. (Vm/s = Vkm/h / 3.6)

def main():
    vel_kmph = int(input("Velocidade em km/h: "))
    print(f'{vel_kmph} km/h = {kpmh_to_ms(vel_kmph):.2f} m/s')

def kpmh_to_ms(v):
    return v / 3.6


main()