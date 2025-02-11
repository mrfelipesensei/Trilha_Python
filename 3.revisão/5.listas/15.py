#Dada uma lista de números [a, b, c, d], crie uma nova lista onde cada elemento seja o produto acumulado dos anteriores:
#Exemplo: [2, 3, 4] → [2, 6, 24]

lista1 = []
lista2 = []

while True:
    try:
        num = float(input("Digite um número para a lista: "))
        if num == 0:
            break

        lista1.append(num)

    except ValueError:
        print("Valor inválido. Digite um número.")

if not lista1:
    print("A lista está vazia. Não é possível calculcar os produtos acumulados.")
else:
    produto_acumulado = 1 #Inicializando a variável com valor 1
    for num in lista1:
        produto_acumulado *= num #Multiplica a variável pelo número atual num
        lista2.append(produto_acumulado) #Adiciona a variável à lista2


print("Lista original:",lista1)
print("Lista com produtos acumulados:",lista2)