import tools

def pi(n):
    if n % 2 == 0:
        return True
    else:
        return False

v = tools.cria_matriz_quadrada(5)


for item in v:
    print(item)

print()
# c = 1
# for i in range(len(v)):
#     for j in range(len(v[i])):
#         if pi(i) or pi(j):
#             v[i][j] = c
#         else:
#             v[i][j] = c + 1
#         print(v[i][j], end='   ')
#     print()
tam = len(v)
c = 0
for i in range(len(v)):
    for j in range(len(v[i])):
        if i ==0 or j ==0:
            v[i][j] = 1
        if i == tam-1 or j == tam-1:
            v[i][j] =   1
        print(v[i][j], end='   ')
    c += 1
    print()