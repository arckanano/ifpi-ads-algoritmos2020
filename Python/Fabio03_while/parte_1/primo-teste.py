def main():

    def eh_primo(n):
        qtd_divisores = 0
        contador = 1
        while contador <= n:
            print(f'{n} % {contador}')
            if n % contador == 0:
                qtd_divisores += 1
            contador += 1
        if qtd_divisores == 2:
            return True
        else:
            return False

    inicio = int(input('Limite inferior: '))
    fim = int(input('Limite superior: '))

    while inicio <= fim:
        if eh_primo(inicio) == True:
            print(inicio)
        inicio += 1


main()
