import math
numeros = input("Digite uma lista de números separados por vírgula: ").split(",")

numeros = [int(num) for num in numeros]

media = sum(numeros) / len(numeros)

print("A média dos números na lista é:", media)