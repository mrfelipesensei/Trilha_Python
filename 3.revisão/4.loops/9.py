#Peça ao usuário informar quantos números deseja inserir. Depois, peça esses números um por um e calcule a média
quantidade = int(input("Digite a quantidade de números: "))

soma = 0
contador = 0

while contador < quantidade:
    numero = int(input("Digite a nota: "))
    soma += numero #valor atual + numero
    contador += 1 #valor atual + 1

media = soma / contador 

print("A média dos números é: ",media)