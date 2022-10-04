https://www.beecrowd.com.br/judge/pt/custom-problems/view/1715

tipocliente = int(input())
ValorCompra = float(input())

if tipocliente == 1:
    preco = ValorCompra
    print("Valor total a ser pago: R$%.2f" %preco)
elif tipocliente  == 2:
    preco = ValorCompra - (ValorCompra*0.13)
    print("Valor total a ser pago: R$%.2f" %preco)
elif tipocliente == 3:
    preco = ValorCompra - (ValorCompra*0.07)
    print("Valor total a ser pago: R$%.2f" %preco)
else:
    print("OPÇÃO INVÁLIDA!")
    )