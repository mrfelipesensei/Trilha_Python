#Crie uma lista de números e calcule a soma e a média dos valores
numeros = []

while True:
    try:
        numero = int(input("Digite um número: "))
        numeros.append(numero)
        if numero == 0:
            break
    except ValueError:
        print("Valor inválido. Digite um número inteiro")

'''
soma = sum(numeros)
media = soma / len(numeros) #soma dos números / quantidade de números obtida pelo len()

print("A soma dos números:",soma)
print("Média dos números:",media)

#Erro - a função len(numeros) está contanto também o zero
'''

numeros.remove(0)
soma = sum(numeros)
media = soma/len(numeros)

print("Soma dos números:",soma)
print("Média dos números:",media)