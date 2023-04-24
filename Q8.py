import math
numeros = input("Digite uma lista de números separados por vírgula: ").split(",")

numeros = [int(num) for num in numeros]

maior = max(numeros)
menor = min(numeros)

print("O maior número da lista é:", maior)
print("O menor número da lista é:", menor)