import math

numeros = input("Digite uma lista de números separados por vírgula: ").split(",")

numeros = [int(num) for num in numeros]

x = int(input("Digite um número para verificar se está presente na lista: "))

if x in numeros:
    print(x, "está presente na lista.")
else:
    print(x, "não está presente na lista.")
