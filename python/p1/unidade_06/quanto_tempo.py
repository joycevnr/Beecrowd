def quanto_tempo(horario1, horario2):
    h1, m1 = horario1.split(":")
    h2, m2 = horario2.split(":")
    
    dif_hr = int(h2) - int(h1)
    dif_min = int(m2) - int(m1)
    
    if dif_min < 0:
        dif_hr -= 1
        dif_min = (int(m2) + 60) - int(m1)
        
    return f"{dif_hr} hora(s) e {dif_min} minuto(s)"


assert quanto_tempo("07:12", "09:07") == "1 hora(s) e 55 minuto(s)"

print(quanto_tempo("07:12", "09:07"))



# # Diferença entre Dois Horários no Dia

# Crie a função `quanto_tempo(horario1, horario2)` que calcula a diferença
# entre dois horários de um determinado dia. Assumir que os horários (`horario1` 
# e `horario2`) são representados como strings no seguinte formato `hh:mm`, 
# `hh` é a representação de dois dígitos da hora e `mm` é a representação de dois
# dígitos dos minutos. Assumir que os horários utilizam o padrão de 24 horas e que
# o `horario2` nunca é menor do que o `horario1`.

# A função retorna uma string com a diferença dos horários. Veja o assert abaixo
# para entender a formatação de saída do retorno da função.

# ## Exemplo e Assert

# ```
# assert quanto_tempo("07:15", "09:18") == "2 hora(s) e 3 minuto(s)"
# ```

# ## Atenção

# Não é permitido usar nenhuma função ou biblioteca de Python que manipule diretamente
# horários e datas.
