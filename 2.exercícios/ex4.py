num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

peso1 = int(input("Digite o peso 1: "))
peso2 = int(input("Digite o peso 2: "))
peso3 = int(input("Digite o peso 3: "))

mediap = ((num1*peso1)+(num2*peso2)+(num3*peso3))/(peso1+peso2+peso3)

print(f"A média ponderada é: {mediap}")