def main():

    inicio = int(input('Limite inferior: '))
    fim = int(input('Limite superior: '))
    resultado(inicio, fim)


def resultado(inicio, fim):
    contador = 1
    divisores = 0
    while contador <= fim:
        if inicio % contador == 0:
            divisores += 1
        contador += 1

    print(divisores)

main()
