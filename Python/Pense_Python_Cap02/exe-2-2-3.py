# saida = 6:52
# 1 kilometro a 8min15s * 2 = 16min30s
# 3 kilometros a 7min12s * 3 = 21min36s
# Total em minutos e segundos = 38min06s

# converter tudo para segundos
total_em_segundos = (38 * 60) + 6
print("Total em segundos {} s".format(total_em_segundos))

# converter para minutos e segundos
minutos = total_em_segundos // 60
segundos = total_em_segundos % 60

print("Trajeto levou {} min e {} s".format(minutos, segundos))

# tempo inicial para minutos
horas_para_minutos = (6 * 60) + 52

# somando tempo inicial com tempo do trajeto
chegou_em = minutos + horas_para_minutos

# convertendo de minutos para hora
horario = chegou_em // 60
horario_s = chegou_em % 60

# hora da chegada
print("Chegou as {}H {}Min {}s".format(horario, horario_s, segundos))