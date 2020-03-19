def main():
    val1 = int(input("valor 1: "))
    val2 = int(input("valor 2: "))

    print("soma: ", add(val1,val2))
    print("subtração: ", sub(val1,val2))
    print("Multiplicação: ", mult(val1, val2))
    print("Divisão: ", div(val1,val2))


def add(a,b):
    soma = a + b
    return soma

def sub(a,b):
    menos = a - b
    return menos

def mult(a,b):
    result = a * b
    return result

def div(a,b):
    dividir = a / b
    return dividir

main()
