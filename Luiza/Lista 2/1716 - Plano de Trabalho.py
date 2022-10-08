# https://www.beecrowd.com.br/judge/pt/custom-runs/code/396558

#entrada de dados

planoFunc =  input()
sal_atual = float(input())

#processamento

if   planoFunc == "a" or planoFunc == "A":
        sal_novo = sal_atual + (sal_atual * 0.10)

elif planoFunc == "b" or planoFunc == "B":
        sal_novo = sal_atual + (sal_atual * 0.15)

elif planoFunc == "c" or planoFunc == "C":
        sal_novo = sal_atual + (sal_atual * 0.20)

print("Novo salário: R$%.2f" % (sal_novo))