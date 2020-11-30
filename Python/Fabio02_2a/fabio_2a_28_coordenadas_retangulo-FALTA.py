def main():
    '''
    Leia as coordenadas cartesianas (x e y) de 2 (dois) pontos no plano, que corresponderão a dois cantos de um retângulo. Baseado nisto, calcule e escreva a área deste retângulo. Lembre-se de que o valor da área não pode ser negativo
    '''
    x1 = int(input("x1: "))
    y1 = int(input("y1: "))

    x2 = int(input("x2: "))
    y2 = int(input("y2: "))

    # Calculo area
    area = ((x1 + x2) * (y1 + y2))
    if area < 0:
        area = area * -1
        print("Area do retangulo: %d " % area)
    else:
        print("Area do retangulo: %d " % area)


    


main()
