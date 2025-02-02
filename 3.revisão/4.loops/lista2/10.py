#Peça um número ao usuário e verifique se ele é perfeito
#A soma de seus divisores - excluindo ele mesmo - é igual ao próprio número

num = int(input("Digite um número para verificar se é perfeito: "))

#Inicializa a soma dos divisores
soma_divisores = 0

#Loop para encontrar os divisores - exceto o próprio número
for i in range(1,num): #vai de 1 até o num
    if num % i == 0: #se i for um divisor de num
        soma_divisores+=i #soma o divisor

#Verifica se a soma dos divisores é igual ao número
if soma_divisores == num:
    print(f"{num} é um número perfeito!")
else:
    print(f"{num} NÃO é um número perfeito.")