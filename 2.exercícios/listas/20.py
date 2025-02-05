#Dada uma lista de números [3,7,2,8,5,10,6], crie uma nova lista apenas com os valores maiores que 5

numeros = [3,7,2,8,5,10,6]
new_numeros = []

for numero in numeros:
    if numero > 5:
        new_numeros.append(numero)
    
print("Números maior que 5: ")
print(new_numeros)