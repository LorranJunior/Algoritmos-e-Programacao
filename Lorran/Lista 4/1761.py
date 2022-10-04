https://www.beecrowd.com.br/judge/pt/custom-problems/view/1761


compras = 0
troco = 0

while True: 
    n = float(input())
    
    if n == 0:
        n1 = float(input())
        troco = n1 - compras
        break 
    
    else: 
        compras = compras + n 
        
print("Total da compra: R$%.2f" %(compras))
print("Valor pago: R$%.2f" %(n1))
print("Troco: R$%.2f" %(troco))