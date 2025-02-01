#Peça dois números ao usuário e exiba todos os números primos entre eles
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
'''
if n1 > 1 and n2 > 1:
    primo = True

    for i in range(n1,n2+1): #Esse loop percorre todos os números de n1 até n2
        if n1 % i == 0 and n2 % i == 0:
            primo = False
        break
'''
#Garante que n1 seja sempre o menor número:
if n1>n2:
    n1,n2 = n2,n1

print(f"Números primos entre {n1} e {n2}:")

#Percorre todos os números do intervalo
for num in range(n1,n2+1):
    if num < 2: #números menores que 2 não são primos
        continue

    primo = True #Assume que o número é primo
    for i in range(2,int(num**0.5)+1): #verifica a divisibilidade até a raiz quadrada de num
        if num % i == 0:
            primo = False
            break #Se encontrar um divisor, não precisa continuar verificando - não é primo

    if primo: #Se primo ainda for True, imprime o número
        print(num, end=" ")


