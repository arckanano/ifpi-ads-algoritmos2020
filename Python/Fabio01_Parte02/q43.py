# Equações lineares

# Entrada de dados
a = int(input('a: '))
b = int(input('b: '))
c = int(input('c: '))
d = int(input('d: '))
e = int(input('e: '))
f = int(input('f: '))

# calculos
x = (c*e) -(b*f) / (a*e) - (b*d)
y = (a*f) - (c*d) / (a*e) - (b*d)

# Saida
print('x = {} e y = {}'.format(x,y))
