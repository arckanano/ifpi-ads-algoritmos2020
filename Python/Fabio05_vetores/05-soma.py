import tools


def main():

    vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    
    
    soma = 0
    i = len(vetor)-1
    j = 0
    while i >= len(vetor) / 2:
        # d = vetor[j] - vetor[i]
        # q = d ** 2
        d = sub2(vetor[j], vetor[i])
        q = pot(d)
        soma += q
        i -= 1
        j += 1

    print(f'Soma = {soma}')

def sub2(a, b):
    return a - b


def pot(x):
    return x ** 2


main()
