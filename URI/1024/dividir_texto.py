def dividir_texto(texto):
    primeira_metade = ''
    segunda_metade = ''

    metade_do_texto = len(texto) // 2
    for letra in range(len(texto)):
        if letra < metade_do_texto:
            primeira_metade += texto[letra]
        elif letra >= metade_do_texto:
            segunda_metade += texto[letra]
    print(primeira_metade)
    print(segunda_metade)
    print(primeira_metade + segunda_metade)



dividir_texto('guilherme')