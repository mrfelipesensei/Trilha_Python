#Peça ao usuário 3 números, exiba-os de forma crescente, decrescente, o maior e o menor
n1 = int(input("Digite o 1º número: "))
n2 = int(input("Digite o 2º número: "))
n3 = int(input("Digite o 3º número: "))

#Criando uma lista com números
numeros = [n1,n2,n3]

#Encontrando o maior e o menor número
maior = max(numeros)
menor = min(numeros)

#Ordenando a lista de forma crescente e decrescente
crescente = sorted(numeros)
decrescente = sorted(numeros,reverse=True)

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
print(f"Em ordem crescente: {crescente}")
print(f"Em ordem decrescente: {decrescente}")
