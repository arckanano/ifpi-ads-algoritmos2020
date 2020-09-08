def main():
    '''
    Criptografia
    Criar 3 funções:
        1 - mover todas as letras 3 casas para a DIREITA
        2 - inverter o texto
        3 - mover todo caracteres da metade em diante 1 posição para a ESQUERDA
    '''
    texto = 'Texto #3'
    texto_para_direita = ''
    texto_invertido = ''
    texto_para_esquerda = ''

    # correr 3 casas para a direita
    print('3 casas para direita:')
    for letra in texto:
        texto_para_direita += chr(ord(letra) + 3)
    print(texto_para_direita)

    print()
    # inverter texto
    print('Texto Invertido')
    for l in range(len(texto)-1, -1, -1):
        texto_invertido += texto[l]
    print(texto_invertido)

    print()
    # para a esquerda
    print('Texto movido para esquerda -1 casa')
    for letra in texto:
        texto_para_esquerda += chr(ord(letra) - 1)
    print(texto_para_esquerda)


    
    primeira_metade = ''
    segunda_metade = ''
    metade_do_texto = len(texto) // 2
    for letra in range(len(texto)):
        # print(letra) # imprime indice
        if letra < metade_do_texto:
            primeira_metade += texto[letra]
        else:
            segunda_metade += texto[letra]
    print(primeira_metade)
    print(segunda_metade)


main()
