#Peça ao usuário um número N e some todos todos os números de 1 até N que sejam múltiplos de 3

n = int(input("Digite um número: "))

'''
lógica do múltiplo
if n%3 == 0:
    print(f"{n} é múltiplo de 3")
elif n%3 == 1:
    print(f"{n} não é múltiplo de 3")
'''
soma = 0
i = 0
cont_mul = 0

while i < n: #enquanto i for menor que o número digitado pelo usuário
    i+=1 #variável de incrementação
    if i%3 == 0: #verificação de múltiplo de 3
        cont_mul+=1 #contagem do número múltiplo de 3
        soma += i #soma do número múltiplo de 3 contado

print(f"A soma dos múltiplos de 3 de 1 à {n} é: {soma}")