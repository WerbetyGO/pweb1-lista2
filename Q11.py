import math
numeros = input("Digite uma lista de números separados por vírgula: ").split(",")

numeros = [int(num) for num in numeros]

imp = [num for num in numeros if num % 2 != 0]

print("Os números impares na lista são:", imp)