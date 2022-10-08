# https://www.beecrowd.com.br/judge/pt/custom-runs/code/403556

cont = 1
total = 0

while cont != 0:
    val_prod = float(input())
    cont = cont + 1
    total = total + val_prod

    if val_prod == 0:
        cont = 0
        val_pag = int(input())

troco = val_pag - total

print("Total da compra: R$%.2f" % (total))
print("Valor pago: R$%.2f" % (val_pag))
print("Troco: R$%.2f" % (troco))
