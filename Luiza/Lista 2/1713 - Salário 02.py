# https://www.beecrowd.com.br/judge/pt/custom-runs/code/395076
valor_h = float(input())
num_h = float(input())

salario_b =(valor_h * num_h)
inss = (salario_b) * 0.08
imp_renda = (salario_b) * 0.11
sindicato = (salario_b) * 0.05
sal_liq = (salario_b - (inss + sindicato + imp_renda))

print("Salário bruto: R$%.2f" % (salario_b))
print("Imposto: R$%.2f" % (imp_renda))
print("INSS: R$%.2f" % (inss))
print("Sindicato: R$%.2f" % (sindicato))
print("Líquido: R$%.2f " % (sal_liq))
