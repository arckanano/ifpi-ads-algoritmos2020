def main():

    n = int(input("Numero: "))

    centena = n // 100
    r = n % 100

    dezena = r // 10
    unidade = r % 10

    if n > 99 and n <= 1000:
        print("{} = {} centenas, {} dezenas e {} unidades".format(n, centena, dezena, unidade))
    elif n > 9 and n < 100:
        print("{} = {} dezenas e {} unidades".format(n, dezena, unidade))
    elif n > 0 and n < 10:
        print("{} = {} unidades".format(n, unidade))
    else:
        print("Favor inserir numero entre 1 e 1000 apenas")

main()
