def main():

    n = int(input('Quantidade de eleitores: '))
    print('--- CANDIDATOS ---')
    print('1 - Candidato 01\n2 - Candidato 02\n3 - Candidato 03\n9 - Voto NULO\n0 - Voto em BRANCO\n')

    candidato01 = 0
    candidato02 = 0
    candidato03 = 0
    votos_nulos = 0
    votos_branco = 0

    for i in range(1, n+1):
        option = int(input('Voto: '))
        if option == 1:
            candidato01 += 1
        elif option == 2:
            candidato02 += 1
        elif option == 3:
            candidato03 += 1
        elif option == 9:
            votos_nulos += 1
        elif option == 0:
            votos_branco += 1

    print('--- CONTAGEM DE VOTOS ---')
    print(f'Candidato 01 - {candidato01} votos\nCandidato 02 - {candidato02} votos\nCandidato 03 - {candidato03} votos\nVotos Nulos = {votos_nulos}\nVotos em Branco: {votos_branco}')
    print()
    print('--- VENCEDOR ---')
    if candidato01 > candidato02 and candidato01 > candidato03:
        print('CANDIDATO 01 - VENCEU')
    elif candidato02 > candidato01 and candidato02 > candidato03:
        print('CANDIDATO 02 - VENCEU')
    elif candidato03 > candidato01 and candidato03 > candidato02:
        print('CANDIDATO 03 - VENCEU')
    else:
        print('>>>>> Segundo Turno <<<<<')


main()
