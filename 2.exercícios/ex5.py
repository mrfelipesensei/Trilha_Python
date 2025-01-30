num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num1 > 0 and num2 > 0:
    print("Ambos são positivos")
elif num1 > 0 or num2 > 0:
    print("Pelo menos um é positivo")
else:
    print("Ambos são negativos.")
