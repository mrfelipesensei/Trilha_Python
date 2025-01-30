#Peça dois números ao usuário e exiba quais números entre eles são pares e quais são ímpares
print("Intervalo de Números: ")
n1 = int(input("Digite o 1º número: "))
n2 = int(input("Digite o 2º número: "))

print(f"Os números pares de {n1} a {n2} são: ")

for i in range(n1,n2+1):
    if i%2 == 0:
        print(i)
    
print(f"Os números ímpares de {n1} a {n2} são: ")

for i in range(n1,n2+1):
    if i%2 != 0:
        print(i)