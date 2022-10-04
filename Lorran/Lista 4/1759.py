https://www.beecrowd.com.br/judge/pt/custom-problems/view/1759


entrada = int(input())

# Salário em 2005
salarioBase = 1000.00 

# Aumento inicial
percentual = 0.015 

# Se o ano informado for < 2005 informa erro
if entrada < 2006:
    print("O ano informado deverá ser > 2005!")

# Caso contrário
else:
    
    # Salário em 2006
    salarioAumento = salarioBase + percentual * salarioBase
    
    # Percorre ano a ano até o ano informado
    for cont in range(2007, entrada + 1):
        
        # Aumenta em 1% o percentual de aumento
        percentual = percentual + 0.01
        
        # Aplica o novo aumento em cima do valor recebido no ano passado
        salarioAumento = salarioAumento + percentual * salarioAumento

    print("Salário Atual: R$%.2f" %(salarioAumento))
        