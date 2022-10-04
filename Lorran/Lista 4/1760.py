https://www.beecrowd.com.br/judge/pt/custom-problems/view/1760


qtdpessoa = 4
cont90 = 0
idade = 0 

for cont in range (qtdpessoa):
    idade1 = int(input())
    Peso = float(input())
    
    if Peso > 90:
        cont90 = cont90 + 1
        idade = idade1 + idade
        
    else:
        idade = idade1 + idade
        
    
media = idade / 4    
print("Qtd pessoas > 90 Kg: %i" %(cont90))
print("Idade média: %.2f" %(media))