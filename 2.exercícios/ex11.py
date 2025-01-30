#solicita o valor a ser sacado
valor = int(input("Digite o valor a ser sacado: "))

#verifica se o valor é zero
if valor == 0:
    print("Nenhum valor a sacar. Operação encerrada.")
else:
    #inicializa a quantidade de cédulas
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


    #exibe a quantidade de cédulas necessárias
    print("Cédulas necessárias: ")
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
