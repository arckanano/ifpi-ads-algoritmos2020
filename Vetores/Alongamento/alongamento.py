qtd_num = int(input("Quantidade de números: "))


def cria_vetor(qtd):
    vetor = [-1] * qtd
    i = 0
    for i in range(len(vetor)):
        vetor[i] = int(input("Numero: "))
    # while i < qtd:
    #     novo_numero = int(input("Numero: "))
    #     vetor.append(novo_numero)
    #     i += 1
    return vetor


def dados(vetor):
    total_par = 0
    total_impar = 0
    total_negativos = 0
    total_positivos = 0
    for i in range(len(vetor)):
        if par_impar(vetor[i]) == True:
            total_par += 1
        else:
            total_impar += 1
        if positivo_negativo(vetor[i]) == True:
            total_positivos += 1
        else:
            total_negativos += 1

    print(f'Números Pares: {total_par}\nNúmeros Ímpares: {total_impar}\nNumeros Positivos: {total_positivos}\nNúmeros Negativos: {total_negativos}')


def media_vetor(vetor):
    soma = 0
    for i in range(len(vetor)):
        soma += vetor[i]
    media = soma / len(vetor)
    return media


def dobra_divide(vetor):
    for i in range(len(vetor)):
        if par_impar(vetor[i]) == True:
            vetor[i] *= 2
        else:
            vetor[i] /= 2

    return vetor


def par_impar(numero):
    if numero % 2 == 0:
        return True
    else:
        return False


def positivo_negativo(numero):
    if numero >= 0:
        return True
    else:
        return False

vet = cria_vetor(qtd_num)

print(f'\nVetor original = {vet}')
print(f'\nDados do Vetor original: ')
dados(vet)

x = dobra_divide(vet)

print(f'\nNovo Vetor {x}')
print(f'\nDados do Novo vetor: ')
dados(x)
print(f'\nMedia do Novo Vetor: {media_vetor(x)}')
