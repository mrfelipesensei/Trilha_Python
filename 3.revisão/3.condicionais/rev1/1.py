#Verifique se um número fornecido pelo usuário é positivo, negativo ou zero
num = float(input("Digite um número: "))

if num > 0:
    print(f"{num} é positivo")
elif num < 0:
    print(f"{num} é negativo")
else:
    print(f"{num} é igual à zero")