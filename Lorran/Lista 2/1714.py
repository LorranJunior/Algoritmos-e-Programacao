#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1714


ValorCompra = float(input())

Lucro = ValorCompra + (ValorCompra*0.45)
Lucro1 = ValorCompra + (ValorCompra*0.30)

if ValorCompra < 20: 
    print("Valor de Venda: R$%.2f" %(Lucro))

else:
    print("Valor de venda: R$%.2f" %(Lucro1))