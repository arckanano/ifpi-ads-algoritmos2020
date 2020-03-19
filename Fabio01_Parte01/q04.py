# 4 - Leia o valor do dólar e um valor em dólar, calcule e escreva o equivalente em real (R$).
#
# Entradas: valor dólar, valor em dólar
valor_do_dolar = float(input("Valor do dólar: "))
qtd_dolares = float(input("Quantidade de dólares: "))

# converter dólar para real
conversor = valor_do_dolar * qtd_dolares

# resultado
print(f'U$ {qtd_dolares:.2f} = R$ {conversor:.2f}')