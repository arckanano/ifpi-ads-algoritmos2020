import dbm
import pickle

alunos = []
pessoas = dbm.open('pessoas.db', 'c')

nome = str(input('Nome: '))
idade = int(input('Idade: '))
email = str(input('E-mail: '))

aluno = {'nome':nome, 'idade':idade, 'email':email}
## Jogar o dicionário gerado dentro da lista de alunos
alunos.append(aluno)
pessoas['alunos'] = pickle.dumps(alunos)

print(pessoas.get('alunos'))
print()
banco_recuperado = pickle.loads(pessoas.get('alunos'))
print(banco_recuperado)
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