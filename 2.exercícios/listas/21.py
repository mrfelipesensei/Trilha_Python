#Crie um programa que recebe uma lista de números e retorne uma nova lista com o quadrado de cada número

numeros = []

for i in range(5):
    while True:
            try:
                numero = int(input(f"Digite o {i+1}º número: "))
                numeros.append(numero)
                break
            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")

'''
for numero in numeros:
    quadrado = numero**2
    print(quadrado)
'''

quadrado = []

for numero in numeros:
    result = numero**2
    quadrado.append(result)

print("Lista com o quadrado de cada número: ")
print(quadrado)