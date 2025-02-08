#Peça ao usuário duas listas de números
#Contatene-as em uma terceira lista

lista1 = []
lista2 = []

while True:
    try:
        numero1 = int(input("Digite um número para a lista I: "))
        lista1.append(numero1)

        if numero1 == 0:
            break

    except ValueError:
        print("Valor inválido. Digite um número inteiro.")

lista1.remove(0)

print(lista1)

while True:
    try:
        numero2 = int(input("Digite um número para a lista II: "))
        lista2.append(numero2)

        if numero2 == 0:
            break

    except ValueError:
        print("Valor inválido. Digite um número inteiro.")

lista2.remove(0)

print(lista2)

lista3 = lista1 + lista2

print(lista3)