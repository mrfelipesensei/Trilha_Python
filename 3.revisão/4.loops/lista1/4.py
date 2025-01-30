#Peça ao usuário um número e exiba a tabuada de 1 a 10 usando o for
numero = int(input("Digite um número para ver sua tabuada: "))

print(f"Tabuada de {numero}:")

for i in range(1,11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")