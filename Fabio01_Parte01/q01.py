# 1 - Leia uma velocidade em m/s, calcule e escreva esta velocidade em km/h. (Vkm/h = Vm/s * 3.6)
#
def main():
    velocidade = float(input("Velocidade em m/s: "))
    vel_em_kmph = converter(velocidade)
    print(f'{velocidade} m/s = {vel_em_kmph} kmph')

def converter(v):
    r = v * 3.6
    return r


main()