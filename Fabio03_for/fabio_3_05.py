# 5. Leia um número, calcule e escreva seu fatorial.
def main():

    n = 10
    fatorial(n)

def fatorial(n):
    for i in range(n, 0, -1):
        fat = i * fatorial(i - 1)
            print(fat)


main()