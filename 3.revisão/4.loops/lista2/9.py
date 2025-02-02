#Peça ao usuário 5 números e diga qual foi o maior número digitado
maior = float('-inf') #Inicializa com um valor muito pequeno - garante que qualquer número será maior
menor = float('inf') #Inicializa com um valor muito grande - garante que qualquer número será menor
i = 0

while i < 5:
    i+=1
    
    num = int(input("Digite um número: "))

    if num > maior: #Atuliza o maior número, se necessário
        maior = num

    if num < menor: #Atualiza o menor número, se necessário
        menor = num

print("O maior número é:",maior)
print("O menor número é:",menor)