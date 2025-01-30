#Peça ao usuário um número e exiba a tabuada de 1 a 10 usando o while
numero = int(input("Digite um número para ver sua tabuada: "))

print(f"Tabuada de {numero}")
'''
i = 1
while i < 11:
    resultado = numero * i
    print(f"{numero}x{i} = {resultado}")
'''

i = 1
while i <= 10:
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    i+= 1 #incrementa o valor de i a cada iteração