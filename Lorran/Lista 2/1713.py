#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1713


A = float (input())
B = float(input())

Soma = A * B 
Inss = (Soma * 8 / 100)
IMPOSTO = (Soma * 11 / 100)
SINDICATO = (Soma * 5 / 100)
LIQUIDO = (Soma * 76 / 100)


print("Salário bruto: R$%.2F" %(Soma))
print("Imposto: R$%.2f" %(IMPOSTO))
print("INSS: R$%.2F" %(Inss))
print("Sindicato: R$%.2f" %(SINDICATO))
print("Líquido: R$%.2f" %(LIQUIDO))