def main():

    s = input()
    marsExploration(s)


def marsExploration(s):
    c = 0
    for i in range(len(s)):
        if s[i] not in 'SO':
            c += 1
    return c


main()
