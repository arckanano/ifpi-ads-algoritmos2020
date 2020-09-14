# TODO: Verificar porque a entrada no site está dando erro

def funnyStrings(s):
    q = int(input()) # quantidade de entradas
    c = 0
    while c < q:
        # texto = input('Texto: ')
        r = reverse(s)
        # print('Lista texto normal: ', gera_lista(texto))
        # print('Lista texto invertido: ', gera_lista(r))
        if gera_lista(s) == gera_lista(r):
            print('Funny')
        else:
            print('Not Funny')
        c += 1


def gera_lista(s):
    dif = []
    a = 0
    b = 0
    for i in range(len(s)):
        if i >= len(s)-1:
            break
        else:
            # print(f'{s[i]}>>>{ord(s[i])}')
            a = ord(s[i])
            b = ord(s[i+1])
            d = a - b
            if d < 0:
                d = d * (-1)
            dif.append(d)
            # print(f'A: {a}; B: {b}')
    # print(dif)
    return dif


def reverse(t):
    r = ''
    for i in range(len(t)-1, -1, -1):
        r += t[i]
    # print('texto invertido', r)
    return r


funnyStrings()
