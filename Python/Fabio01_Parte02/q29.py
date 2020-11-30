# Leia um número inteiro de meses, calcule e escreva quantos anos e quantos meses ele corresponde.

# Entradas
Meses = int(input('Meses: '))

# Processamento
qtdAno = Meses // 12
qtdMes = Meses % 12

# Saida
print('{} ano(s) e {} mes(es).'.format(qtdAno, qtdMes))
