# https://www.beecrowd.com.br/judge/pt/custom-runs/code/397851

nomeFunc = str(input())  # o usuário vai digitar o seu nome
horas_ext_trab = float(input())  # o usuário vai digitar o n° de horas trabalhadas

sal_min = 1192.40  # valor do lário mínimo
valor_hora_ext = 10.00  # valor da hora extra
sal_hr_ext = horas_ext_trab * valor_hora_ext  # valor do salário minimo + horas extras
sal_br = 3 * sal_min + sal_hr_ext  # valor do salário bruto (sal_min + valor_hora_extra)

# Calculo INSS
if sal_br > 2000:
    inss = sal_br * 0.12  # 12% de desconto do salário bruto se for maior que R$2000.00
else:
    INSS = sal_br * 0.05

# Calculo Imposto Renda
if sal_br > 2500:
    imposto_r = sal_br * 0.20
else:
    imposto_r = sal_br * 0

sal_liq = sal_br - inss - imposto_r

print("Nome: %s" % (nomeFunc))
print("Salário bruto: R$%.2f" % (sal_br))
print("Salário líquido: R$%.2f" % (sal_liq))