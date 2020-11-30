def soma2(a,b):
    return a + b


def subtrai2(a,b):
    return a - b


def divide2(a,b):
    return a / b

def multiplica2 (a, b):
    return a * b

def resto_da_divisao(a,b):
    return a % b

def acha_centena(n):
    '''
    Função válida para números de 3 dígitos
    '''
    return n // 100


def acha_dezena(n):
    '''
    Função válida para números de 3 dígitos
    '''
    return (n % 100) // 10


def acha_unidade(n):
    '''
    Função válida para números de 3 dígitos
    '''
    return (n % 100) % 10

def calculo_imc(altura, peso):
    imc = divide2(peso, (altura**2))
    if imc < 25:
        return print("peso normal")
    elif imc >= 25 and imc < 30:
        return print("obeso")
    else:
        return print("Obesidade morbida")

# Inicio funções para calculo de equações do 2o grau
def delta(a, b, c):
    return ((b ** 2) - 4 * a * c)

def raiz1(a, b, c):
    return (-b + (delta(a, b, c) ** (1 / 2))) / (2 * a)

def raiz2(a, b, c):
    return (-b - (delta(a, b, c) ** (1 / 2))) / (2 * a)