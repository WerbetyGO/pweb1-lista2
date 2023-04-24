import math
num = int(input("Insira um número inteiro: "))

a, b = 0, 1

while b <= num:
    print(b, end=' ')
    a, b = b, a+b