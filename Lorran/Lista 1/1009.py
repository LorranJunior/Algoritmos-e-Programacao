#https://www.beecrowd.com.br/judge/pt/problems/view/1009

n = input()
salario = float(input())
vendas = float(input())

st = salario + 0.15*vendas

print("TOTAL = R$",'{:.2f}'.format(st))