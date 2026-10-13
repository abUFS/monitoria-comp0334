tempo_segundos = int(input())

horas = tempo_segundos // 3600
minutos = (tempo_segundos % 3600) // 60
segundos = tempo_segundos % 60

print('%d:%d:%d' % (horas, minutos, segundos))