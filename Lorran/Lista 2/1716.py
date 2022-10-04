#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1716

SalarioAtual = input()
NovoSalario = float(input())

if SalarioAtual == "A":
    saldo = NovoSalario + (NovoSalario*0.10)
    print("Novo salário: R$%.2f" %saldo)
elif SalarioAtual  == "B":
    saldo = NovoSalario + (NovoSalario*0.15)
    print("Novo salário: R$%.2f" %saldo)
elif SalarioAtual == "C":
    saldo = NovoSalario + (NovoSalario*0.20)
    print("Novo salário: R$%.2f" %saldo)
else:
    print("OPÇÃO INVÁLIDA!")