# https://www.beecrowd.com.br/judge/pt/runs/code/30215270

num = int(input())
horas = num // 60**2
num = num - horas * 60**2

minutos = num // 60
num = num - minutos * 60

segundos = num

print("%i:%i:%i"% (horas, minutos, segundos))