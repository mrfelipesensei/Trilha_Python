#Dada uma lista com elementos repetidos, remova as duplicadas e exiba a lista sem repetições

lista = ["banana","uva","laranja","maçã","banana","kiwi","jambo"]

'''for fruta in lista:
    if lista.count(fruta) > 1:
        print("TESTE")'''

nova_lista = []

for fruta in lista:
    if lista.count(fruta) == 1: #Verifica se a fruta aparece apenas uma vez na lista
        nova_lista.append(fruta)
    elif fruta not in nova_lista: #Verifica se a fruta já foi adicionada à nova lista
        nova_lista.append(fruta)

print(nova_lista)