#Faça um programa que rotacione os elementos
#para a direita em uma posição

lista = [1,2,3,4,5]

'''while True:
    roda = input("Digite ok para rodar: ")
    
    if roda.lower() == "ok":
        lista[0] = lista[4]
        print(lista)

    lista.remove(lista[4])
    print(lista)'''

while True:
    roda = input("Digite 'ok' para rodar: ")
    ultimo_elemento = lista[-1] #Obtém o último elemento da lista

    if roda.lower() == "ok":
        ultimo_elemento = lista.pop() #Remove e retorna o último elemento
        lista.insert(0,ultimo_elemento) #Insere o último elemento no início

        print(lista)
    else:
        print("Entrada inválida. Digite 'ok' para rotacionar a lista.")


    

    

        
