# 11 - Leia um número inteiro (3 dígitos) e escreva o inverso do número. (Ex.: número = 532 ; inverso = 235)
numero = int(input("Número: "))

# Quebrar o número em unidade, dezenas e centenas
centena = numero // 100
dezenas = (numero % 100) // 10
unidade = (numero % 100) % 10

# converter para string
centena = str(centena)
dezenas = str(dezenas)
unidade = str(unidade)

# concatenar tudo
inverso = unidade + dezenas + centena

# resultado
print(f'{numero} ao contrário é {inverso}')