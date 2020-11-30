# 2 - Leia um valor em horas e um valor em minutos, calcule e escreva o equivalente em minutos.

def main():
    valor_horas = int(input("Horas: "))
    valor_minutos = int(input("Minutos: "))
    total_em_minutos = transforma_em_minutos(valor_horas, valor_minutos)
    print(f'Total em minutos: {total_em_minutos}')

def transforma_em_minutos(h, m):
    return (h * 60) + m


main()