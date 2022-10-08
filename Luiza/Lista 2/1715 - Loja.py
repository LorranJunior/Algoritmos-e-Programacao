# https://www.beecrowd.com.br/judge/pt/custom-runs/code/396529

#entrada de dados
tipo_cliente = int(input())
valor_total = float(input())

#processamento
if tipo_cliente == 1:
    print("Valor total a ser pago: R$%.2f" % valor_total)                        # >>> cliente comum
elif tipo_cliente == 2:
    print("Valor total a ser pago: R$%.2f" %(valor_total - valor_total * 0.13))  # >>> funcionário
elif tipo_cliente == 3:
    print("Valor total a ser pago: R$%.2f" % (valor_total - valor_total * 0.07)) # >>> cliente premium

#saída
else: print("OPÇÃO INVÁLIDA!")