# 4 - Leia o valor do dólar e um valor em dólar, calcule e escreva o equivalente em real (R$).
#
def main():
    valor_em_dolar = float(input("Valor em dólar: "))
    valor_do_dolar = float(input("Valor do dólar: "))

    resultado = conversor_de_moedas(valor_em_dolar, valor_do_dolar)
    
    print(f'U${valor_em_dolar:.2f} = R${resultado:.2f}')

def conversor_de_moedas(valor_a_se_convertido, cotacao):
    return valor_a_se_convertido * cotacao

main()