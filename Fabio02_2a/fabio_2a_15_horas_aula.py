def main():

    horasProfA = int(input("Horas aula do(a) professor(a) A: "))
    valorHoraProfA = int(input("Valor hora aula: "))
    horasProfB = int(input("Horas aula do(a) professor(a) B: "))
    valorHoraProfB = int(input("Valor hora aula: "))

    salarioA = horasProfA * valorHoraProfA
    salarioB = horasProfB * valorHoraProfB

    if salarioA > salarioB:
        print("O professor(a) A recebe mais que o professor(a) B")
    else:
        print("O professor(a) B recebe mais que o professor(a) A")


main()
