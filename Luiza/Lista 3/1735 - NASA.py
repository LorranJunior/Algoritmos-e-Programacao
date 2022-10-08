# https://www.beecrowd.com.br/judge/pt/custom-runs/code/397784

valor_inicial = int(input())  # inicial
valor_final = int(input())  # final

while valor_inicial >= valor_final:
    print(valor_inicial)
    valor_inicial = valor_inicial - 1

print("Fogo!")
