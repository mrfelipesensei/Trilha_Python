#Dada a tupla frutas = ('maçã','banana','uva','laranja','manga')
#Exiba os três primeiros elementos
#Exiba os elementos de índice 2 até o final
#Inverta a tupla e exiba o resultado

frutas = ('maçã','banana','uva','laranja','manga')
print(frutas[0:3])
print(frutas[2:5])

tupla_invertida = tuple(reversed(frutas))
print(tupla_invertida)