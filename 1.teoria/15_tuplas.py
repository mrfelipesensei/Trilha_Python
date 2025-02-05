#Tuplas são estruturas de dados semelhantes a listas
#MAS são IMUTÁVEIS - seus elementos não podem ser alterados após a criação

#São úteis para armazenar conjuntos de dados que não devem ser modificados

#Criando Tuplas
#Tuplas são definidas com parênteses () ou sem qualquer delimitador:

#Tupla com parênteses
tupla1 = (1,2,3,4)

#Tupla sem parênteses (tuple packing)
tupla2 = "a","b","c"

#Tupla de um único elemento (vírgula obrigatória)
tupla3 = (5,)

#Criando com a função tuple()
tupla4 = tuple([1,2,3])

#Acessando Elementos
#É feito pelos índices - como nas listas

print(tupla1[0])
print(tupla2[-1])

#Fatiamento
#Tuplas suportam slicing

print(tupla1[1:3])

#Operações com Tuplas
nova_tupla = tupla1 + tupla2
print(nova_tupla)

repetida = tupla1 * 2
print(repetida)

#Desempacotamento
#Você pode atribuir os valores da tupla a variáveis

a,b,c = tupla2
print(a,b,c)

#Ou ignorar valores usando _

a,_,c = tupla2
print(a,c)

#Funções Úteis:
print((len(tupla1))) #Tamanho da tupla
print(min(tupla1)) #Menor valor
print(max(tupla1)) #Maior valor
print(tupla1.count(2)) #Contagem de ocorrências do número2
print(tupla1.index(3)) #Índice do número 3