# https://www.beecrowd.com.br/judge/pt/custom-runs/code/397691

num = int(input())  # Digite o valor de n:
# 5! = 5 * 4 * 3 * 2 * 1
# 0!=1

fat = 1
i = 2
while i <= num:
    fat = fat * i
    i = i + 1

print("%i! = " % num, fat)
