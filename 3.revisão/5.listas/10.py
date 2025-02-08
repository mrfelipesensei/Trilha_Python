#Dadas duas listas de números
#Crie uma nova lista contendo apenas os números que aparecem em ambas

lista1 = [1,2,3]
lista2 = [5,2,4]
lista3 = []

'''
for num1 in lista1:
    lista3.append(num1)

for num2 in lista2:
    lista3.append(num2)'''

for num1 in lista1: #Se o num1 estiver na lista1
    if num1 in lista2: #Se o num1 estiver na lista2
        lista3.append(num1) #Se num1 estiver na lista1 e lista2, adicione-o a lista3

print(lista3)