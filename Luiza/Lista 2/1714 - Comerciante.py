# https://www.beecrowd.com.br/judge/pt/custom-runs/code/395084
valor_produto = (float(input()))

if valor_produto < 20:
    venda = valor_produto * 1.45
else:
    venda = valor_produto * 1.30

print('Valor de venda: R$%.2f' %(venda))
