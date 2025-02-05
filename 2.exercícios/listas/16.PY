#Peça ao usuário para digitar 5 números e armazene-os em uma lista
'''
i = 0
numeros =[]

while i < 5:
    numero = int(input("Digite um número"))
    i+=1
    for numero in numeros:
        print(numeros)
'''
#Lista vazia para armazenar os números
numeros = []

#Loop para pedir 5 números ao usuário
for i in range(5):
    while True:
        try:
            numero = int(input(f"Digite o {i+1}º número: "))
            numeros.append(numero)
            break
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")

print("Números digitados:",numeros)
