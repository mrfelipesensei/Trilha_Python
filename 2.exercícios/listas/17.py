#Crie um programa que verifique se um determinado número está presente na lista
numeros = [1,2,4,5,6,7,8,6,7,13,14,179,45,789,84,32,56,45,95,75,10245,14568]

'''
for numero in numeros:
    if numero == 13:
        print(numero)
'''

numero_procurado = 13

#Variável para controlar se o número foi encontrado
encontrado = False

#Percorre a lista e verifica se o número está presente
for elemento in numeros:
    if elemento == numero_procurado:
        encontrado = True
        break #Sai do loop se o número for encontrado

if encontrado:
    print(f"O número {numero_procurado} está presente na lista.")
else:
    print(f"O número {numero_procurado} não está presente na lista.")