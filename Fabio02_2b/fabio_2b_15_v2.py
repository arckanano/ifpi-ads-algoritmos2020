def main():

    peso_morango = float(input("Peso morango: "))
    peso_maca = float(input("Peso maçã: "))
    peso_total = peso_maca + peso_morango

    # Calcular preço total da compra
    valor_de_maca = 0.0
    valor_de_morango = 0.0
    if peso_morango <= 5:
        valor_de_morango = 2.50 * peso_morango
    else:
        valor_de_morango = 2.20 * peso_morango
    if peso_maca <= 5:
        valor_de_maca = 1.80 * peso_maca
    else:
        valor_de_maca = 1.50 * peso_maca

    valor_total_da_compra = valor_de_maca + valor_de_morango

    # calculo se tem desconto
    desconto = 0.0
    if peso_total > 8 or valor_total_da_compra > 25:
        desconto = valor_total_da_compra * 0.10
        valor_total_da_compra = valor_total_da_compra - desconto

    print(f'Valor de morango: {valor_de_morango:.2f}')
    print(f'Valor de maçã: {valor_de_maca:.2f}')
    print(f'Valor do desconto: {desconto:.2f}')
    print(f'Valor Total: R${valor_total_da_compra:.2f}')


main()
