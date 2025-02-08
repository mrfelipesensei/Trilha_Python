num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

if num1 == num2 and num2 == num3:
    print("Todos são iguais")
elif num1 == num2 or num1 == num3 or num2 == num3:
    print("Pelo menos dois são iguais.")
elif num1 != num2 and num1 != num3 and num2 != num3:
    print("Todos são diferentes.")