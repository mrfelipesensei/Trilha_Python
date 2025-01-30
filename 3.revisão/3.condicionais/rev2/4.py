#Peça ao usuário 3 números, exiba-os de forma crescente, decrescente, o maior e o menor
n1 = int(input("Digite o 1º número: "))
n2 = int(input("Digite o 2º número: "))
n3 = int(input("Digite o 3º número: "))
'''
maior = 0

if n1>n2 and n1>n3:
    maior = n1
elif n2>n1 and n2>n3:
    maior = n2
elif n3>n1 and n3>n2:
    maior = n3

print(f"O maior número é: {maior}")
    
if n1<n2 and n1<n3 and n2<n3:
    print(f"Crescente: {n1,n2,n3}")
elif n2<n1 and n2<n3 and n1<n3:
    print(f"Crescente: {n2,n1,n3}")
elif n3<n1 and n3<n2 and n2<n1:
    print(f"Crescente: {n3,n2,n1}")
elif n2>n3 and n3<n1 and n2<n1:
    print(f"Crescente: {n2,n3,n1}")
'''

maior = n1
if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

menor = n1
if n2 < menor:
    menor = n2
if n3 < menor:
    menor = n3

if n1 <= n2 <= n3:
    ordem_crescente = n1,n2,n3
elif n1 <= n3 <= n2:
    ordem_crescente = n1, n3, n2
elif n2 <= n1 <= n3:
    ordem_crescente = n2,n1,n3
elif n2 <= n3 <= n1:
    ordem_crescente = n2,n3,n1
elif n3 <= n1 <= n2:
    ordem_crescente = n3,n1,n2
else:
    ordem_crescente = n3,n2,n1

#Ordenando em ordem descrescente - Invertendo a ordem crescente
ordem_decrescente = ordem_crescente[::-1]

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
print(f"Em ordem crescente: {ordem_crescente}")
print(f"Em ordem decrescente: {ordem_decrescente}")