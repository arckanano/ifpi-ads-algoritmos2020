# Leia um número inteiro (4 dígitos binários), calcule e escreva o equivalente na base decimal

# Entradas
# num = int(input('Número binario (max. 4 digitos): '))

def binToDec():
    num = int(input('Número binario (max. 4 digitos): '))
    if len(str(num)) > 4:
        print("Número muito grande!")
        binToDec()
    else:
        # Processamento
        # Separação das unidades
        milhar = num // 1000
        restoMilhar = num % 1000

        centena = restoMilhar // 100
        restoCentena = restoMilhar % 100

        dezena = restoCentena // 10
        unidade = restoCentena % 10

        # Calculo do binário
        b01 = (2 ** 0) * unidade
        b02 = (2 ** 1) * dezena
        b03 = (2 ** 2) * centena
        b04 = (2 ** 3) * milhar
        decimal = b01+b02+b03+b04

        return decimal

        # Saida
decimal = binToDec()
print(f'R = {decimal}')
# print('{} em binario equivale a {} em decimal'.format(num, decimal))
# TODO corrigir erro quando o programa identifica numero maior que 4 digitos e solicita novo número onde o resultado é NONE