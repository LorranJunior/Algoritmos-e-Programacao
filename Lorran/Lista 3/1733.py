#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1733

# Entrada de Dados
nome = str(input())
qtdExtras = float(input())

SalarioM = 1192.40
vlHrExtras = 10.00

SalHrExtra = qtdExtras * vlHrExtras
SalBruto = 3 * SalarioM + SalHrExtra

# Processamento de Dados

# Calcula o INSS
if SalBruto > 2000:
    inss = SalBruto * 0.12
    
else:
    inss = SalBruto * 0.05
    
# Calcula o Imposto de Renda
if SalBruto > 2500:
    ir = SalBruto * 0.20
    
else: 
    ir = Sal * 0.0

# Calcula o Liquido    
SalarioLiquido = SalBruto - inss - ir


# Saída de Dados
print("Nome: %s" %(nome))
print("Salário bruto: R$%.2f" %(SalBruto))
print("Salário líquido: R$%.2f" %(SalarioLiquido))