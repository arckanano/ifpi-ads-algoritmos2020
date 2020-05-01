import mod_corrigido
import mod_vigente


def main():
    '''
                                Base de cálculo (R$)
    |-----------------------------------------------------------------------|
    | VIGENTE                   | CORRIGIDA                 | ALÍQUOTA (%)  |
    ------------------------------------------------------------------------|
    |até 1.903,98               | até 3.881,65              |   ISENTO      |
    |de 1.903,99 até 2.826,65   | de 3.881,66 até 5.714,11  |   7,5         |
    |de 2.826,66 até 3.751,05   | de 5.714,12 até 7.654,67  |   15          |
    |de 3.751,06 até 4.664,68   | de 7.654,68 até 9.564,42  |   22,5        |
    |acima de 4.664,68          | acima de 9.564,42         |   27,5        |
    |-----------------------------------------------------------------------|
    '''

    salario = float(input("Inserir salário: "))
    mod_vigente.tabela_ir_vigente(salario)
    mod_corrigido.tabela_ir_corrigida(salario)


main()
