#Crie uma lista com 5 números e exiba o primeiro e o último elemento
numeros = [5,7,8,314,27]
print(numeros[0])
print(numeros[4])

#Adicione um número à lista e exiba-a atualizada
numeros.append(84)
print(numeros)

#Remova um número da lista e exiba a nova lista
numeros.remove(numeros[3])
print(numeros)

#Use um loop for para exibir todos os elementos da lista
for numero in numeros:
    print(numero)