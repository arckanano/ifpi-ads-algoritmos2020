import tools


def main():

    novo_vetor = tools.cria_vetor(8)
    #novo_vetor = tools.cria_vetor(4)
    
    meu_vetor = tools.adiciona_valor(novo_vetor)
    decimal = tools.binToDec(meu_vetor)
    hexadecimal = tools.binToHex(meu_vetor)
    print(f'O binário em decimal = {decimal}')
    print(f'O binário em Hexadecimal = {hexadecimal}')
    

main()
