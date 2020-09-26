# Criar vetor
def cria_vetor(tamanho):
    vetor = [0] * tamanho
    return vetor


def adiciona_valor(vetor):
    for i in range(len(vetor)):
        vetor[i] = int(input(f'Insira um valor inteiro na posição {i}: '))
    return vetor


def inverte_vetor(vetor, vetorVazio):
	novo_vetor = vetorVazio
	pos = 0
	for i in range(len(vetor)-1, -1, -1):
		novo_vetor[pos] = vetor[i]
		pos += 1
	return novo_vetor
	