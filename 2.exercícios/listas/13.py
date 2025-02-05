#Crie uma lista com 10 números e exiba apenas os números ímpares
numeros = [1,4,5,9,84,75,459,60,61,64,127,128,32,1,5,45,75,85,975,5]
for numero in numeros:
    if numero%2 != 0:
        print(numero)