def main():

    i = 1
    contador = 1
    while contador <= 10:
        for i in range(11):
            print(f'{contador} + {i} = {contador + i}')
            i += 1
        print('-' * 10)
        contador += 1

main()