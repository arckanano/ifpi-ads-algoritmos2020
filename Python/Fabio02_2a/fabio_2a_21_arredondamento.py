def main():

    num = float(input("numero fracionario: "))

    if num % 1 >= 0.5:
        num = (num // 1) + 1
        print(num)
    else:
        num = num - (num % 1)
        print(num)


main()
