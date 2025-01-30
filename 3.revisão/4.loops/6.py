#Peça um número ao usuário e use um for para verificar se ele é primo
numero = int(input("Digite um número: "))

if numero > 1:
    primo = True

    #Esse loop percorre todos os números de 2 até o número digitado pelo usuário
    for i in range(2,numero):
        if numero % i == 0: #Verifica se o número é divisível por i - Se for, não será primo
            primo = False
        break

    if primo:
        print(numero, "é um número primo.")
    else:
        print(numero, "não é um número primo.")

else:
    print("Um número primo deve ser maior que 1!")