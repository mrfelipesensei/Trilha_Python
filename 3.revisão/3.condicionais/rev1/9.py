#Crie um programa que classifique um triângulo como equilátero, isósceles ou escaleno com base em seus lados
print("Classificação de Triângulos")
lado1 = int(input("Digite o 1º lado: "))
lado2 = int(input("Digite o 2º lado: "))
lado3 = int(input("Digite o 3º lado: "))


if lado1 == 0 or lado2 == 0 or lado3 == 0:
    print("Valores inválidos")
else:
    if lado1 == lado2 and lado2 == lado3:
        print("Triângulo Equilátero")
    elif lado1 == lado2 or lado1 == lado3:
        print("Triângulo Isósceles")
    else:
        print("Triângulo Escaleno")

