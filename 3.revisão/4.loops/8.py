#Peça um número ao usuário e calcule seu fatorial usando for
num = int(input("Digite o número para calcular seu fatorial: "))

fatorial = 1

#loop para multiplicar os números de 1 até o número fornecido
for i in range(1,num+1):
    fatorial *= i

print(f"O fatorial de {num} é {fatorial}")