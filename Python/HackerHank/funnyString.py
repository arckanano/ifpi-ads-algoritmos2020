def funnyString(s):
    c = 0
    while c < 2:
        r = reverse(s)
        if gera_lista(s) == gera_lista(r):
            return 'Funny'
        else:
            return 'Not Funny'
        c += 1


def gera_lista(s):
    dif = []
    a = 0
    b = 0
    for i in range(len(s)):
        if i >= len(s)-1:
            break
        else:
            a = ord(s[i])
            b = ord(s[i+1])
            d = a - b
            if d < 0:
                d = d * (-1)
            dif.append(d)
    return dif


def reverse(t):
    r = ''
    for i in range(len(t)-1, -1, -1):
        r += t[i]
    return r
