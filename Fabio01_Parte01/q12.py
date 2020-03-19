# 12 - Leia o salário de um trabalhador e escreva seu novo salário com um aumento de 25%.

# entrada
salario = float(input("Salário: "))

# Adicionando aumento
novo_salario = salario + ((salario / 100) * 25)

# Resultado
print(f'Novo salário {novo_salario:.2f}')