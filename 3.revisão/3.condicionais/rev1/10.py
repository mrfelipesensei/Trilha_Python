#Simule um sistema de caixa eletrônico que pergunte o valor a ser sacado e informe o número de notas de 100, 50, 20, 10, 5 e 2 necessárias para o saque
print("**SISTEMA DE CAIXA**")
valor = int(input("Digite o valor a ser sacado: "))

if valor == 0:
    print("Nenhum valor a sacar. Operação encerrada.")
else:
    cedulas_100 = valor // 100
    valor %= 100

    cedulas_50 = valor // 50
    valor %= 50

    cedulas_20 = valor // 20
    valor %= 20

    cedulas_10 = valor // 10
    valor %= 10

    cedulas_5 = valor // 5
    valor %= 5

    cedulas_2 = valor // 2
    valor %= 2

if cedulas_100 > 0:
    print(f"R$100: {cedulas_100}")
if cedulas_50 > 0:
    print(f"R$50: {cedulas_50}")
if cedulas_20 > 0:
    print(f"R$20: {cedulas_20}")
if cedulas_10 > 0:
    print(f"R$10: {cedulas_10}")
if cedulas_5 > 0:
    print(f"R$5: {cedulas_5}")
if cedulas_2 > 0:
    print(f"R$2: {cedulas_2}")