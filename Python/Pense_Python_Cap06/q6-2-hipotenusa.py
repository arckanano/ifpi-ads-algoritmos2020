# Retorna o comprimento da hipotenusa dado os doisa lados do triangulo retangulo
def main():

    lado_a = int(input("Tamanho lado a: "))
    lado_b = int(input("Tamanho lado b: "))

    print(hipotenusa(lado_a, lado_b))


def hipotenusa(a, b):
    h = ((a * a) + (b * b)) ** 0.5
    return h



main()