# Se você correr 10 quilômetros em 42 minutos e 42 segundos, qual é o seu passo médio (tempo por milha em minutos e segundos)? Qual é a sua velocidade média em milhas por hora?

distancia_em_km = 10

# descobrir tempo total em segundos
tempo_total_em_segundos = (42 * 60) + 42

# converter km para metros
distancia_percorrida_em_metros = distancia_em_km * 1000

# Descobrir velocidade em metro por segundo
velocidade_em_metros_por_segundo = distancia_percorrida_em_metros / tempo_total_em_segundos

# Coverter metro por segundo em kilometro por hora
metro_segundo_em_kilometro_hora = velocidade_em_metros_por_segundo * 3.6

# Converter de kilometro por hora para milhar por hora
kilometro_hora_em_milha_hora = metro_segundo_em_kilometro_hora / 1.61

# Resultado
print("Tempo médio em milha por hora: {:.2f}".format(kilometro_hora_em_milha_hora))