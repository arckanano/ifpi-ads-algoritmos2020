def main():

    peso_morango = float(input("Peso morango: "))
    peso_maca = float(input("Peso maçã: "))
    peso_total = peso_maca + peso_morango

    if peso_morango <= 5 and peso_maca <= 5:
        preco_morango = 2.5
        preco_maca = 1.80
        valor_compra = (peso_morango * preco_morango) + (peso_maca * preco_maca)
        print("Valor da compra: R$%.2f " % valor_compra)
    elif peso_morango > 5 and peso_maca > 5:
        preco_morango = 2.2
        preco_maca = 1.5
        valor_compra = (peso_morango * preco_morango) + (peso_maca * preco_maca)
        print("Valor da compra: R$%.2f " % valor_compra)
    elif peso_total > 8 or valor_compra > 25:
        preco_morango = 2.2
        preco_maca = 1.5
        valor_compra = (peso_morango * preco_morango) + (peso_maca * preco_maca)
        print("Valor da compra: R$%.2f " % valor_compra)


main()
