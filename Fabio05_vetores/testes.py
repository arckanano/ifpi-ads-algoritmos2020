import tools

vet = [1,0,1,0,1,1,1,1]
vet1 = [] # recebe primeira metade do vetor
vet2 = [] # recebe segunda metade do vetor

for i in range(len(vet)):
    vet1.append(vet[i])
    if len(vet1) % 4 == 0:
        print(vet1)
        vet1.clear()

# for i in range(len(vet)):
#     if i < (len(vet) / 2):
#         vet1.append(vet[i])
#     else:
#         vet2.append(vet[i])

# x = tools.binToDec(vet1)
# y = tools.binToDec(vet2)

# r = ''
# h = [10, 'A', 11, 'B',12,'C',13,'D',14,'E',15,'F']
# for i in range(len(h)):
#     if h[i] == x:
#         r += h[i+1]

# print(r)
