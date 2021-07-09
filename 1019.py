segundos = int(input())
#horas
horas = int(segundos/3600)
segundos -= horas*3600
#minutos
minutos = int(segundos/60)
segundos -= minutos*60

print('{}:{}:{}'.format(horas, minutos, segundos))