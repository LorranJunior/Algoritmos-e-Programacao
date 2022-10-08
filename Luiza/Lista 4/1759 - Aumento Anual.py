# https://www.beecrowd.com.br/judge/pt/custom-runs/code/403407

ano = int(input())

sal_base = 1000
percentual = 0.015
sal_final = 0

if ano < 2006:
    print("O ano informado deverá ser > 2005!")

else:
    sal_2006 = sal_base + percentual
    sal_final = sal_base + (percentual * sal_base)

    for i in range(2007, ano + 1):  # repete de 2007 até ano informado
        percentual = percentual + 0.01
        sal_final = sal_final + (percentual * sal_final)  # calcula novo aumento, dados em cima do ano anterior
    print("Salário atual: R$%.2f" % (sal_final))