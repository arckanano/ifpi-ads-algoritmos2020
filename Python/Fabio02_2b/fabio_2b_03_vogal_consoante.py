def main():
'''
Leia uma letra e verifique se a letra digitada é vogal ou consoante
'''
    l = input("Digite uma letra: ").lower()

    if l == 'a' or l == 'e' or l == 'i' or l == 'o' or l == 'u':
        print("vogal")
    else:
        print("consoante")


main()
