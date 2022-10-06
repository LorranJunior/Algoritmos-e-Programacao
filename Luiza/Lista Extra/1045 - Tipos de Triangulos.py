# https://www.beecrowd.com.br/judge/pt/problems/view/1045
x = input().split()
a, b, c = x

num1 = float(1)
num2 = float(1)
num3 = float(1)
a = float(a)
b = float(b)
c = float(c)

if a >= b and a >= c:
    num1 = a
    if b >= c:
        num2 = b
        num3 = c
    else:
        num2 = c
        num3 = b
if b >= a and b >= c:
    num1 = b
    if a >= c:
        num2 = a
        num3 = c
    else:
        num2 = c
        num3 = a

if c >= a and c >= b:
    num1 = c
    if a >= b:
        num2 = a
        num3 = b
    else:
        num2 = b
        num3 = a

if a == b and b == c:
    num1 = a
    num2 =b
    num3 = c

a = num1
b = num2
c = num3

if a >= (b + c):
    print("NAO FORMA TRIANGULO")
else:
    if (a ** 2) == (b ** 2 + c ** 2):
        print("TRIANGULO RETANGULO")
    if (a ** 2) > (b ** 2 + c ** 2):
        print("TRIANGULO OBTUSANGULO")
    if (a ** 2) < (b ** 2 + c ** 2):
        print("TRIANGULO ACUTANGULO")
    if (a == b == c):
        print("TRIANGULO EQUILATERO")
    if a == b != c or b == c != a or a == c != b:
        print("TRIANGULO ISOSCELES")
