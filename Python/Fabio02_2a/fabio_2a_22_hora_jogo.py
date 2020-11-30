# duração do jogo
def main():

    # horario de inicio
    jogo_hora_inicio = int(input("Hora de inicio: "))
    jogo_minuto_inicio = int(input("Minuto de inicio: "))

    # horario de termino
    jogo_hora_termino = int(input("Hora de termino: "))
    jogo_minuto_termino = int(input("Minuto de termino: "))

    # tempo em minutos em que o jogo iniciou
    hora_de_inicio_em_minutos = converter_tempo_para_minutos(jogo_hora_inicio, jogo_minuto_inicio)

    # tempo  em minutos em que o jogo finalizou
    hora_de_termino_em_minutos = converter_tempo_para_minutos(jogo_hora_termino, jogo_minuto_termino)

    # verrificar se o jogo durou mais ou menos de 24 horas
    tempo_total_do_jogo_em_minutos = hora_de_termino_em_minutos - hora_de_inicio_em_minutos

    # exibir quantas horas durou o jogo
    # converter o tempo total do jogo em minutos em HORAS e MINUTOS
    duracao_hora = acha_hora(tempo_total_do_jogo_em_minutos)
    duracao_minutos = acha_minutos(tempo_total_do_jogo_em_minutos)

    if duracao_hora < 0:
        duracao_hora = 24 + duracao_hora
        print(f'Tempo total do jogo {duracao_hora} horas e {duracao_minutos} minutos')
        print(f'Tempo total do jogo em minutos: {tempo_total_do_jogo_em_minutos}')   
    elif hora_de_termino_em_minutos > hora_de_inicio_em_minutos:
        print(f'Tempo total do jogo {duracao_hora} horas e {duracao_minutos} minutos')
        print(f'Tempo total do jogo em minutos: {tempo_total_do_jogo_em_minutos}')
    elif hora_de_termino_em_minutos == hora_de_inicio_em_minutos:
        print("Duração de 24 horas.")

    # Se incio e termino forem IGUAIS então duração do jogo = 24 horas
    # Se tempo em minutos do termino do jogo MENOR QUE tempo em minutos de INICIO do jogo ENTAO duração do jogo MENOR QUE 24 horas
    # Se termino do jogo em minutos MAIOR que INICIO do jogo em minutos, ENTAO duração do jogo maior que 24 horas => retorna como tempo inválido

    # 1 - passo: converter tudo pra minutos
def converter_tempo_para_minutos(hora, minutos):
    return (hora * 60) + minutos

def acha_hora(minutos):
    return minutos // 60

def acha_minutos(minutos):
    return minutos % 60

        
main()