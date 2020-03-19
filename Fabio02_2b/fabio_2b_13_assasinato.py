def main():

    p1 = input("Telefonou para a vítima ?: ")
    p2 = input("Esteve no local do crime ?: ")
    p3 = input("Mora perto da vítima ?: ")
    p4 = input("Devia para a vítima ?: ")
    p5 = input("Já trabalhou com a vítima ?: ")

    contador = [p1, p2, p3, p4, p5]
    rep = contador.count("sim")

    if rep == 2:
        print("Supeito(a)!")
    elif rep == 3 or rep == 4:
        print("Cúmplice!")
    elif rep == 5:
        print("Assassino!")
    elif rep <= 1:
        print("Inocente!")


main()
