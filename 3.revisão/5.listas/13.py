#Dada uma lista de números
#Encontre o segundo maior
#Sem usar sort()

lista = [10,20,4,45,99,99,5]

#Inicializamos as variáveis com um valor muito baixo
maior = float('-inf')
segundo_maior = ('-inf')

#Percorremos a lista para encontrar o maior e o segundo maior valor
for num in lista:
    if num > maior:
        segundo_maior = maior #O antigo maior vira o segundo maior
        maior = num #Atualiza o maior
    elif segundo_maior < num < maior:
        segundo_maior = num #Atualiza o segundo maior

'''Se o número atual for maior que 'maior' - ele se tornará o novo maior 
e o antigo/anterior maior vira segundo_maior'''
'''Se o número estiver entre 'maior' e 'segundo_maior' ele então será de fato o segundo maior'''

#Verificamos se encontramos um segundo maior válido
segundo_maior = segundo_maior if segundo_maior != float('-inf') else None

print(maior)
print(segundo_maior)