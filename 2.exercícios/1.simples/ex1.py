num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2
prod = num1 * num2
dif = num1 / num2
exp = num1 ** num2
mod = num1 % num2

if num1 > num2:
    maior = num1
elif num2 > num1:
    maior = num2
else:
    maior = None

print(f"A soma é: {soma}")
print(f"O produto é: {prod}")
print(f"A diferença é: {dif}")
print(f"O resto da dividão é: {mod}")
print(f"{num1} elevado à {num2} é: {exp}")

if maior is not None:
    print("O número maior é: {maior}")
else:
    print(f"{num1} e {num2} são iguais")