soma = 0

print("Digite números para somar. 0 para sair.")

while True:
    num = int(input("Digite um número: "))
    if num == 0:
        break

    soma += num

print(f"A soma dos números é: {soma}")