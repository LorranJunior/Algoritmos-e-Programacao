# https://www.beecrowd.com.br/judge/pt/problems/view/1021
nota = float(input())

nota100 = nota // 100
nota = nota - nota100 * 100

nota50 = nota // 50
nota = nota - nota50 * 50

nota20 = nota // 20
nota = nota - nota20 * 20

nota10 = nota // 10
nota = nota - nota10 * 10

nota5 = nota // 5
nota = nota - nota5 * 5

nota2 = nota // 2
nota = nota - nota2 * 2

moeda1 = nota // 1
nota = nota - moeda1 * 1
moeda1 = float("%.2f" % moeda1)
nota = float("%.2f" % nota)

moeda50 = nota // 0.5
nota = nota - moeda50 * 0.5
moeda50 = float("%.2f" % moeda50)
nota = float("%.2f" % nota)

moeda25 = nota // 0.25
nota = nota - moeda25 * 0.25
moeda25 = float("%.2f" % moeda25)
nota = float("%.2f" % nota)

moeda10 = nota // 0.10
nota = nota - moeda10 * 0.10
moeda10 = float("%.2f" % moeda10)
nota = float("%.2f" % nota)

moeda5 = nota // 0.05
nota = nota - moeda5 * 0.05
moeda5 = float("%.2f" % moeda5)
nota = float("%.2f" % nota)

moeda01 = nota // 0.01
moeda1 = float("%.2f" % moeda1)
nota = float("%.2f" % nota)

print("NOTAS:")

print("%i nota(s) de R$ 100.00" % nota100)
print("%i nota(s) de R$ 100.00" % nota50)
print("%i nota(s) de R$ 100.00" % nota20)
print("%i nota(s) de R$ 100.00" % nota10)
print("%i nota(s) de R$ 100.00" % nota5)
print("%i nota(s) de R$ 100.00" % nota2)

print("MOEDAS:")

print("%i nota(s) de R$ 100.00" % moeda1)
print("%i moeda(s) de R$ 0.50" % moeda50)
print("%i moeda(s) de R$ 0.50" % moeda25)
print("%i moeda(s) de R$ 0.50" % moeda10)
print("%i moeda(s) de R$ 0.50" % moeda5)
print("%i moeda(s) de R$ 0.50" % moeda01)
