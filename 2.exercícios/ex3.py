num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

peso1 = 3
peso2 = 2
peso3 = 5

media = (num1 + num2 + num3)/3

mediap = ((num1 * peso1) + (num2 * peso2) + (num3 * peso3)) / (peso1 + peso2 + peso3)

print(f"A média aritimética é: {media}")
print(f"A média ponderada é: {mediap}")
