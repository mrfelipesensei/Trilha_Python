#Dadas duas listas de números
#Crie uma nova lista contendo apenas os números que aparecem em ambas

lista1 = []
lista2 = []
lista3 = []

while True:
    try:
        num1 = int(input("Digite um número para a lista I: "))

        if num1 == 0:
            break

        lista1.append(num1)

    except ValueError:
        print("Valor inválido. Digite um número inteiro.")

while True:
    try:
        num2 = int(input("Digite um número para a lista II: "))

        if num2 == 0:
            break

        lista2.append(num2)

    except ValueError:
        print("Valor inválido. Digite um número inteiro.")

#Encontrando elementos repetidos
for num1 in lista1: #Se o num1 estiver na lista1
    if num1 in lista2 and num1 not in lista3: #Se o num1 estiver na lista2
        lista3.append(num1) #Se num1 estiver na lista1 e lista2, adicione-o a lista3

print(lista3)