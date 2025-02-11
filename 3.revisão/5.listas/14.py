#Dada uma lista de números, crie duas novas listas: uma contendo apenas os pares e outra apenas os ímpares.

lista = []
lista_par = []
lista_impar = []


while True:
    try:
        num = float(input("Digite um número para a lista: "))
        if num == 0:
            break
        
        #Lógica para números pares
        if num % 2 == 0:
            lista_par.append(num)
        elif num % 2 != 0: #Lógica para números ímpares
            lista_impar.append(num)

        lista.append(num)
    except ValueError:
        print("Valor inválido. Digite um número")


print("A lista original é:",lista)
print("A lista de números pares:",lista_par)
print("A lista de números ímpares:",lista_impar)