#Peça o valor de uma compra. Se for maior que R$100 aplique um desconto de 10% e mostre o valor final. Caso contrário, exiba o valor sem desconto
valor = float(input("Informe o valor da compra: "))

if valor > 100:
    desconto = valor*0.1
    tot = valor - desconto
    print(f"Sua compra no valor de R${valor} sairá por R${tot}")
else:
    print(f"Compra no valor de R${valor}")