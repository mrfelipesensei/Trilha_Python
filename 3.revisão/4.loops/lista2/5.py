#Peça ao usuário vários números. Quando ele digitar um número negativo, pare o loop e exiba a soma dos positivos
soma = 0
num = 0

while num >= 0:
    try:
        num = int(input("Digite um número: "))
        if num > 0:
            soma+= num
    except ValueError:
        print("Por favor digite um número inteiro!")
else:
    print("FIM")

print("A soma dos números positivos é:",soma)