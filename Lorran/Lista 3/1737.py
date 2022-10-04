https://www.beecrowd.com.br/judge/pt/custom-problems/view/1737


somaNum = 0
qtdNum = int(input())
contador = 0

if qtdNum <= 0:
    print("Informe uma quantidade > 0!")
else: 
    while contador < qtdNum:
        NumDig = float(input())
        somaNum = somaNum + NumDig
        contador = contador + 1
        
    print("Soma dos números informados: %.2f" %(somaNum))