# 3 - Leia um valor em minutos, calcule e escreva o equivalente em horas e minutos.
#
def main():
    valor_em_minutos = int(input("Valor em minutos> "))
    transformar(valor_em_minutos)


def transformar(m):
    horas = m // 60
    minutos = m % 60
    print(f'{m} min = {horas} h e {minutos} m')


main()