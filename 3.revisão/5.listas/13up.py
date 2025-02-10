#Dada uma lista de números
#Encontre o segundo maior
#Sem usar sort()

lista = []

while True:
    try:
        num = float(input("Digite um número para a lista: "))
        if num == 0:
            break

        lista.append(num)
    except ValueError:
        print("Valor inválido. Digite um número: ")


#Inicializamos as variáveis com um valor muito baixo
maior = float('-inf')
segundo_maior = float('-inf')

#Inicializa as variáveis com o maior valor possível
menor = float('inf')
segundo_menor = float('inf')

#Percorremos a lista para encontrar o maior e o segundo maior valor
for num in lista:
    if num > maior:
        segundo_maior = maior #O antigo maior vira o segundo maior
        maior = num #Atualiza o maior
    elif segundo_maior < num < maior:
        segundo_maior = num #Atualiza o segundo maior

    #Lógica para menor e segundo menor
    if num < menor:
        segundo_menor = menor
        menor = num
    elif segundo_menor > num > menor:
        segundo_menor = num
        

'''Se o número atual for maior que 'maior' - ele se tornará o novo maior 
e o antigo/anterior maior vira segundo_maior'''
'''Se o número estiver entre 'maior' e 'segundo_maior' ele então será de fato o segundo maior'''

#Verificamos se encontramos um segundo maior válido
segundo_maior = segundo_maior if segundo_maior != float('-inf') else None
#Verificamos se encontramos um segundo menor válido
segundo_menor = segundo_menor if segundo_menor != float('inf') else None

print("O maior número é:",maior)
print("O segundo maior número é:",segundo_maior)
print("O menor número é:",menor)
print("O segundo menor número é:",segundo_menor)

'''-inf é os números vindos do infinito negativo
inf são os números vindos do infinito positivo'''