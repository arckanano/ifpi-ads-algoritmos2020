import functions
# 11 - Leia um número inteiro (3 dígitos) e escreva o inverso do número. (Ex.: número = 532 ; inverso = 235)

def main():
    numero = int(input("Número: "))

    centena = str(functions.acha_centena(numero))
    dezenas = str(functions.acha_dezena(numero))
    unidade = str(functions.acha_unidade(numero))

    # concatenar tudo
    inverso = unidade + dezenas + centena

    # resultado
    print(f'{numero} ao contrário é {inverso}')


main()