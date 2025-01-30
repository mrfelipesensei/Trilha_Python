num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

#soma e mantém somente a parte inteira
soma = int(num1 + num2)

if num1 > num2:
    maior = num1
elif num2 > num1:
    maior = num2
else:
    maior = None #caso sejam iguais

print(f"A soma é {soma}")

if maior is not None:
    print(f"O maior número é {maior}")
else:
    print("Os números são iguais")