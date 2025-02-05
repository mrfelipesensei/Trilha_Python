#Crie um programa que verifique se um determinado número está presente na lista
numeros = [1,2,3,4,5]
numero = int(input("Digite um número: "))

if numero in numeros:
    print(f"{numero} está na lista!")
else:
    print(f"{numero} não está na lista!")