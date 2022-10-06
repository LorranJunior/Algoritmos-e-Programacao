# https://www.beecrowd.com.br/judge/pt/problems/view/1019
num = int(input())
horas = num // 60**2
num = num - horas * 60**2

minutos = num // 60
num = num - minutos * 60

segundos = num

print("%i:%i:%i"% (horas, minutos, segundos))