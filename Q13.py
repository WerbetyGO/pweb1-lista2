import math
numeros = input("Digite uma lista de números separados por vírgula: ").split(",")

numeros = [int(num) for num in numeros]

numeros.sort()

print("Os números na lista em ordem crescente são:", numeros)
