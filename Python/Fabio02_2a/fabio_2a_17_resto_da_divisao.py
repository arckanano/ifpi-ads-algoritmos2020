def main():

    v1 = int(input("v1: "))
    v2 = int(input("v2: "))

    resto = v1 % v2
    if resto != 1 and resto != 2 and resto != 3 and resto != 4 :
        qv1 = v1**2
        qv2 = v2**2
        print("quadrado v1: {}".format(qv1))
        print("quadrado v2: {}".format(qv2))
    elif resto == 1:
        soma = v1 + v2 + resto
        print("soma: ", soma)
    elif resto == 2:
        print("v1 é: ", pi(v1))
        print("v2 é: ", pi(v2))
    elif resto == 3:
        mult = (v1 + v2) * v1
        print("multiplicação: ", mult)
    elif resto == 4:
        div = (v1 + v2) / v2
        print("divisão: ", div)


def pi(x):

    if x % 2 == 0:
        return("par")
    else:
        return("impar")

main()
