#Crie uma lista de frutas, adicione "banana" no final e remova a primeira fruta
frutas = ["maçã","laranja","uva","pêra","kiwi"]
frutas.append("banana")
frutas.remove(frutas[0])

for fruta in frutas:
    print(fruta)