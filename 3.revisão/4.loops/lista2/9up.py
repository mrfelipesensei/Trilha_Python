#Peça ao usuário 5 números e diga qual foi o maior número digitado
num = 0
numeros = [] #Lista vazia para armazenar os números
i = 1

'''
while i <= 5:
    num = input("Digite um número: ")    
    i+=1

    numeros = [num]

    maior = max(numeros)
    menor = min(numeros)

print(maior)
'''

while i <= 5: #Loop que pede 5 números ao usuário
    num = int(input("Digite um número: "))
    i+=1

    numeros.append(num) #Adiciona o número à lista

#procura o número maior e o menor
maior = max(numeros)
menor = min(numeros)

print("O maior número digitado foi:",maior)
print("O menor número foi:",menor)