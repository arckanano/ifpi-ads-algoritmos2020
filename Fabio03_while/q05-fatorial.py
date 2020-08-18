def main():

    n = int(input('Numero: '))

    contador = n
    a = 1
    while contador > 1:
        a *= contador
        contador -= 1
    print(f'{n}! = {a}')
    
main()