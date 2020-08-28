def main():

    n = int(input('Quantidade de fichas: '))

    maior_peso = 0
    menor_peso = 0
    id_maior = ''
    id_menor = ''
    for i in range(1, n+1):
        num_id = int(input('Número de identificação: '))
        nome = input('Nome: ')
        peso = float(input('Peso: '))
        if peso > maior_peso:
            maior_peso = peso
            id_maior = num_id
            menor_peso = peso
        if peso < menor_peso:
            menor_peso = peso
            id_menor = num_id

    print(
        f'ID mais magro = {id_menor} | Peso: {menor_peso}\nID mais gordo = {id_maior} | Peso: {maior_peso}')


main()
