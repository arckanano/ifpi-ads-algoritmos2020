def soma2(a,b):
    return a + b


def subtrai2(a,b):
    return a - b


def divide2(a,b):
    return a / b


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