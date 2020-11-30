import dbm
import pickle

alunos = []
pessoas = dbm.open('pessoas.db', 'c')

# nome = str(input('Nome: '))
# idade = int(input('Idade: '))
# email = str(input('E-mail: '))

# aluno = {'nome':nome, 'idade':idade, 'email':email}
# ## Jogar o dicionário gerado dentro da lista de alunos
# alunos.append(aluno)

# ## Adicionar a lista de Alunos no banco usando uma chave
# x = str(input("Nome da chave: "))
# pessoas[x] = pickle.dumps(alunos)

# ## Fechar o banco para salvar as alterações
# pessoas.close()

## Reabrindo para fazer a leitura
pessoas = dbm.open('pessoas.db', 'r')

##
for key in pessoas:
    person = pickle.loads(pessoas.get(key))
    print(person[0]['email'])

## R
# print(pessoas.get('aluno2'))
# print()
# banco_recuperado = pickle.loads(pessoas.get('aluno2'))
# print(banco_recuperado)

## Fechando banco após a leitura
pessoas.close()

# aluno_str = pickle.dumps(aluno)
# print(aluno_str)
# aluno_recuperado = pickle.loads(aluno_str)
# print(aluno_recuperado)
# print(type(aluno_recuperado))

# Salvando no banco de dados no formato de String usando pickle.dumps()
# pessoas['aluno_1'] = pickle.dumps(aluno)
# print(pessoas['aluno_1'])
# print(pessoas.get('aluno_1'))

# # Recuperando 
# aluno_recuperado = pickle.loads(pessoas['aluno_1'])
# print(aluno_recuperado)