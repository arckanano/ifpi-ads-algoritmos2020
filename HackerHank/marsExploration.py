def main():

    s = input()
    marsExploration(s)


def marsExploration(s):
    palavra = 'SOS'
    sub = ''
    e = 0
    for i in range(len(s)):
        sub += s[i]
        if len(sub) % 3 == 0:
            for j in range(len(sub)):
                if sub[j] != palavra[j]:
                    e += 1
            sub = ''
    return e


main()
