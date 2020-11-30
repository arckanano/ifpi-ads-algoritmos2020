def main():

    n = int(input('Total de eleitores: '))

    tot = bozo = ciro = haddad = branco = nulo = 0

    while tot < n:
        print('1 - Bozo\n2 - Ciro\n3 - Haddad\n9 - Nulo\n0 - Branco')

        v = int(input('Escolha candidato: \n'))

        if v == 1:
            bozo += 1
        elif v == 2:
            ciro += 1
        elif v == 3:
            haddad += 1
        elif v == 9:
            nulo += 1
        elif v == 0:
            branco += 1
        else:
            nulo += 1

        tot += 1

    print('--- Resultado da Eleição ---')
    print(f'Bozo = {bozo} votos')
    print(f'Ciro = {ciro} votos')
    print(f'Haddad = {haddad} votos')
    print(f'Nulos = {nulo} votos')
    print(f'Branco = {branco} votos')

    if bozo > ciro and bozo > haddad:
        print('Vencedor = Bozo')
    elif ciro > bozo and ciro > haddad:
        print('Vencedor = Ciro')
    elif haddad > ciro and haddad > bozo:
        print('Vencedor = Haddad')
    else:
        print('--- 2º Turno ---')


main()
