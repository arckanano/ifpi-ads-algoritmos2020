#TODO: ERROU, ERROU FEIO, ERROU RUDE!!!!
def main():

    p1 = str(input("Telefonou para a vítima ?: "))
    p2 = str(input("Esteve no local do crime ?: "))
    p3 = str(input("Mora perto da vítima ?: "))
    p4 = str(input("Devia para a vítima ?: "))
    p5 = str(input("Já trabalhou com a vítima ?: "))

    if p1 != p2 and p1 != p3 and p1 != p4 and p1 != p5 or p2 != p3 and p2 != p4 and p2 != p5 or p3 != p4 and p3 != p5 or p4 != p5:
        print("Inocente")
    elif p1 == p2 or p1 == p3 or p1 == p4 or p1 == p5 or p2 == p3 or p2 == p4 or p2 == p5 or p3 == p4 or p3 == p5 or p4 == p5:
        print("Suspeita")
    elif p1 == p2 == p3 or p1 == p2 == p4 or p1 == p2 == p5 or p2 == p3 == p4 or p2 == p3 == p5 or p3 == p4 == p5:
        print("Cumplice")
    elif p1 == p2 == p3 == p4 or p1 == p2 == p3 == p5 or p1 == p2 == p4 == p5 or p1 == p3 == p4 == p5 or p2 == p3 == p4 == p5:
        print("Cumplice")
    elif p1 == p2 and p1 == p3 and p1 == p4 and p1 == p5:
        print("Culpado")



main()
