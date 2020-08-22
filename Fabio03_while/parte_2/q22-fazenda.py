def main():

    ficha = int(input('Número de fichas: '))

    contador = 1
    maior_peso = 0
    menor_peso = 0
    nome_maior = ''
    nome_menor = ''
    while contador <= ficha:
        nome = input('Nome: ')
        peso = float(input('Peso do boi [kg]: '))
        if peso > maior_peso:
            maior_peso = peso
            nome_maior = nome
        if peso < maior_peso:
            menor_peso = peso
            nome_menor = nome
        contador += 1

    print(f'Boi mais pesado: {nome_maior} com {maior_peso}Kg')
    print(f'Boi mais magro: {nome_menor} com {menor_peso}Kg')


main()
