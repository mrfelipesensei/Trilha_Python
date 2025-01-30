#Peça um número ao usuário e informe se ele é positivo, negativo ou zero
n = float(input("Digite um número: "))

if n > 0:
    print(f"{n} é positivo")
elif n < 0:
    print(f"{n} é negativo")
else:
    print(f"{n} é zero.")