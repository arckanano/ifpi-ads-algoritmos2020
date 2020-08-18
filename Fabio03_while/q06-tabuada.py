def main():

    # Exibir tabuada dos 10 primeiros números

    def soma(n=10):
        contador = 1
        while contador <= n:
            s = contador + n
            print(f'{s} + {contador} = {s}')
            contador += 1
    

    def sub(n=10):
        contador = 1
        while contador <= n:
            s = n - contador
            print(f'{n} - {contador} = {s}')
            contador += 1


    def multiplicar(n=10):
        contador = 1
        while contador <= n:
            m = contador * n
            print(f'{n} * {contador} = {m}')
            contador += 1


    def div(n=10):
        contador = 1
        while contador <= n:
            d = n // contador
            print(f'{n} / {contador} = {d}')
            contador += 1


    def resultados():
        print('--- Tabuada de soma ---')
        soma()
        print('--- Tabuada de subtração ---')
        sub()
        print('--- Tabuada de multiplicação ---')
        multiplicar()
        print('--- Tabuada de divisão ---')
        div()


    resultados()


main()
