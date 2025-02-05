#O que são Listas em Python?
#Uma lista é uma estrutura que armazena vários valores dentro de um único nome - variável

frutas = ["maçã","banana","uva"]
print(frutas)

#Cada item tem um índice - começando em 0
print(frutas[0]) #primeiro item (maçã)
print(frutas[1]) #segundo item (banana)

#Como adicionar e remover elementos?
#Adicionar
frutas.append("laranja")
print(frutas)

#Remover
frutas.remove("uva")
print(frutas)

#Percorrendo uma lista com for
#Se quisermos imprimir todos os elementos da lista - usamos um loop for
for fruta in frutas:
    print(fruta)