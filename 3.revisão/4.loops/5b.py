#Peça dois números ao usuário e exiba quais números entre eles são pares e quais são ímpares
print("Intervalo de números: ")
n1 = int(input("Digite o 1º número: "))
n2 = int(input("Digite o 2º número: "))

i = n1

print(f"Os números pares de {n1} a {n2} são: ")
while i <= n2:
    if i%2 == 0:
        print(i)
    i+=1 #incrementa o valor de i a cada iteração!

i = n1 #Reinicia i para o primeiro número do intervalo

print(f"Os números ímpares de {n1} a {n2} são: ")
while i <= n2:
    if i%2 != 0:
        print(i)
    i+= 1 #incrementa o valor de i a cada iteração!