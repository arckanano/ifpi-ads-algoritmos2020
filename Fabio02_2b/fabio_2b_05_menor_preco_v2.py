def main():
    '''
    Leia o preço de três produtos e informe qual produto deve ser comprado, sabendo que a decisão é sempre pelo mais barato.
    '''
    produto_1 = float(input("Valor produto 1: "))
    produto_2 = float(input("Valor produto 2: "))
    produto_3 = float(input("Valor produto 3: "))

    confere = menor(produto_1, produto_2, produto_3)

    print(f'Produto com menor valor = {confere}')

def menor(v1, v2, v3):
    menor = v1
    if v2 < menor:
        menor = v2
    if v3 < menor:
        menor = v3
    return menor

main()
