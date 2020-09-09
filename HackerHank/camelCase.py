def main():

    s = 'saveChangesInTheEditor'
    print(camelcase(s))


def camelcase(s):
    total = 1
    for i in range(len(s)):
        if ord(s[i]) >= 65 and ord(s[i]) <= 90:
            total += 1
    return total


main()

# Solução enviada ao HackerHank
# https://www.hackerrank.com/challenges/camelcase/submissions/code/178618925