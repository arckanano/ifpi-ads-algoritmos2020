import functions

def main():
    val1 = int(input("valor 1: "))
    val2 = int(input("valor 2: "))

    soma = functions.soma2(val1, val2)
    subtracao = functions.subtrai2(val1, val2)
    multiplicacao = functions.multiplica2(val1, val2)
    divisao = functions.divide2(val1, val2)

    print(f"soma: {soma}")
    print(f"subtração: {subtracao}")
    print(f"Multiplicação: {multiplicacao}")
    print(f"Divisão: {divisao}")

main()
