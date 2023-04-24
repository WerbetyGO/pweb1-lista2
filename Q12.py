import math
numeros = input("Digite uma lista de números separados por vírgula: ").split(",")

numeros = [int(num) for num in numeros]

soma = sum(numeros)

print("A soma dos números na lista é:", soma)