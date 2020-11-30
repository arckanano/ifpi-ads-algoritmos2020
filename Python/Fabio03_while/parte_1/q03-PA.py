def main():

    a = int(input('Valor inicial A: '))
    limite = int(input('Limite: '))
    razao = int(input('razão: '))

    contador = a
    while contador <= limite:
        print(contador, end=' ')
        contador += razao
    print('ACABOU!!!')


main()
